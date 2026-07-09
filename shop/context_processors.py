from django.conf import settings


def shop_info(request):
    """Makes shop business details available in every template."""
    return {
        'SHOP_NAME': settings.SHOP_NAME,
        'SHOP_PHONE': settings.SHOP_PHONE,
        'SHOP_WHATSAPP': settings.SHOP_WHATSAPP,
        'SHOP_ADDRESS': settings.SHOP_ADDRESS,
    }
