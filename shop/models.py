from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def saree_count(self):
        return self.sarees.count()


class Saree(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='sarees')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                     help_text="Optional. Shown as a struck-through original price.")
    fabric = models.CharField(max_length=120, blank=True, help_text="e.g. Kanjivaram Silk, Banarasi Silk")
    description = models.TextField()
    is_featured = models.BooleanField(default=False, help_text="Show in the Featured Sarees section on Home")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this saree from the website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Saree.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def primary_image(self):
        img = self.images.filter(is_primary=True).first()
        if not img:
            img = self.images.first()
        return img

    def discount_percent(self):
        if self.old_price and self.old_price > self.price:
            return round(((self.old_price - self.price) / self.old_price) * 100)
        return 0

    def whatsapp_message(self):
        return (
            "Hello ,\n"
            "I want to order this saree.\n"
            f"Product: {self.name}\n"
            f"Price: Rs. {self.price}\n"
            "My Name: \n"
            "My Mobile: "
        )


class SareeImage(models.Model):
    saree = models.ForeignKey(Saree, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='sarees/')
    is_primary = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"Image for {self.saree.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at:%d %b %Y}"
