# Contact/context_processors.py
from django.conf import settings

def stripe_keys(request):
    return {
        # this makes STRIPE_PUBLISHABLE_KEY available in every template
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
    }
