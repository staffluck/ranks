from django.urls import path

from .views import BuyItemView


urlpatterns = [
    path("buy/<int:pk>/", BuyItemView.as_view())
]
