from django.urls import path

from .views import BuyItemView, ItemDetailView


urlpatterns = [
    path("buy/<int:pk>/", BuyItemView.as_view()),
    path("item/<int:pk>/", ItemDetailView.as_view())
]
