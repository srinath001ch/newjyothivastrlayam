from django.contrib import admin
from .models import Category, Saree, SareeImage, ContactMessage


class SareeImageInline(admin.TabularInline):
    model = SareeImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'saree_count')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Saree)
class SareeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_featured', 'is_active', 'created_at')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SareeImageInline]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    readonly_fields = ('created_at',)
