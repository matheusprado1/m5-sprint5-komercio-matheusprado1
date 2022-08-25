from django.urls import path

from . import views

urlpatterns = [
    path("accounts/", views.AccountView.as_view()),
    path("accounts/<uuid:pk>/", views.AccountRetriveUpdateDestroyAPIView.as_view()),
    path("accounts/<uuid:pk>/management/", views.AccountManagementView.as_view()),
    path("accounts/newest/<int:num>/", views.RetrieveAccountView.as_view()),
    path("login/", views.UserLoginView.as_view()),
]
