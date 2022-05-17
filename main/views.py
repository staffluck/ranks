from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Item
from .stripe_utils import get_stripe_session_id


class BuyItemView(GenericAPIView):

    def get(self, request, pk):
        try:
            item = Item.objects.filter(id=pk)
        except Item.DoesNotExist:
            raise NotFound

        cancel_url = request.build_absolute_uri("")
        success_url = request.build_absolute_uri("")
        session_id = get_stripe_session_id(item, cancel_url, success_url)

        return Response({"session_id": session_id}, 201)
