from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/<uuid:pk>/", views.RetrieveUpdateDestroyAPIView.as_view()),
    ]