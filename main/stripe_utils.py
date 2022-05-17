from django.db.models import QuerySet
from django.conf import settings
import stripe

from .models import Item


stripe.api_key = settings.STRIPE_KEY


def get_stripe_session_id(items: QuerySet[Item], cancel_url: str, success_url: str):

    items_data = []
    for item in items:
        items_data.append(
            {
                "quantity": 1,
                "price_data": {
                    "currency": "USD",
                    "product_data": {
                        "name": item.name,
                        "description": item.description
                    },
                    "unit_amount_decimal": item.price
                },
            }
        )

    session = stripe.checkout.Session.create(
        cancel_url=cancel_url,
        success_url=success_url,
        mode="payment",
        line_items=items_data
    )

    return session.id
