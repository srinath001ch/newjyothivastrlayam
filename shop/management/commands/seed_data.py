from django.core.management.base import BaseCommand
from shop.models import Category, Saree


class Command(BaseCommand):
    help = "Seeds the database with sample categories and sarees so the shop owner can see how the site looks. Safe to run multiple times."

    def handle(self, *args, **options):
        categories_data = [
            ("Kanjivaram Silk", "Rich traditional silk sarees from Tamil Nadu"),
            ("Banarasi Silk", "Opulent sarees with intricate zari work"),
            ("Handloom Cotton", "Comfortable, breathable everyday sarees"),
            ("Designer Sarees", "Contemporary designs for modern women"),
            ("Bridal Collection", "Exquisite sarees for the big day"),
            ("Chiffon & Georgette", "Light, flowy party-wear sarees"),
        ]

        cat_objs = []
        for i, (name, desc) in enumerate(categories_data):
            cat, created = Category.objects.get_or_create(
                name=name, defaults={"description": desc, "order": i}
            )
            cat_objs.append(cat)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created category: {name}"))

        sample_sarees = [
            ("Royal Kanjivaram Silk Saree", cat_objs[0], 12999, 15999, "Pure Kanjivaram Silk", True),
            ("Emerald Banarasi Zari Saree", cat_objs[1], 18999, 22999, "Banarasi Silk", True),
            ("Sunrise Handloom Cotton Saree", cat_objs[2], 2499, None, "Handloom Cotton", False),
            ("Ivory Designer Sequin Saree", cat_objs[3], 8999, 10999, "Georgette", True),
            ("Crimson Bridal Kanjivaram Saree", cat_objs[4], 24999, 29999, "Pure Silk", True),
            ("Blush Pink Chiffon Saree", cat_objs[5], 3999, None, "Chiffon", False),
            ("Golden Temple Border Silk Saree", cat_objs[0], 14999, None, "Kanjivaram Silk", False),
            ("Maroon Banarasi Wedding Saree", cat_objs[1], 20999, 24999, "Banarasi Silk", True),
        ]

        description = (
            "An exquisite handpicked saree crafted with the finest fabric and intricate detailing. "
            "Perfect for weddings, festivals, and special occasions. Each piece reflects timeless "
            "craftsmanship and elegance, making it a must-have addition to your ethnic wardrobe."
        )

        for name, cat, price, old_price, fabric, featured in sample_sarees:
            saree, created = Saree.objects.get_or_create(
                name=name,
                defaults=dict(
                    category=cat, price=price, old_price=old_price, fabric=fabric,
                    description=description, is_featured=featured, is_active=True,
                ),
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created saree: {name}"))

        self.stdout.write(self.style.SUCCESS(
            "\nDemo data ready! Note: sample sarees have no images — add images "
            "for each saree from /dashboard/ so they display correctly on the site."
        ))
