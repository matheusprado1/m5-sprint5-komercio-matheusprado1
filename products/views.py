from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from products.permissions import IsProductOwner

from .models import Product
from .serializers import ProductDetailSerializer, ProductSerializer
from .mixins import SerializerByMixin


class ProductView(SerializerByMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()
    serializer_map = {
        'GET': ProductDetailSerializer,
        'POST': ProductSerializer
    }

    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)


class RetrieveUpdateDestroyAPIView(
    SerializerByMixin, generics.RetrieveUpdateDestroyAPIView
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsProductOwner]

    queryset = Product.objects.all()

    serializer_map = {
        'GET': ProductDetailSerializer,
        'PATCH': ProductSerializer
    }
