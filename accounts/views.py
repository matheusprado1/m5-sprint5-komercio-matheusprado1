from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication

from .models import Account
from .serializers import AccountSerializer, LoginSerializer


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class RetrieveAccountView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        amount_users = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:amount_users]

class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"detail": "invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)