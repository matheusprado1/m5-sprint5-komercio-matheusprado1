from django.urls import path

from .views import AccountManagementView, AccountRetriveUpdateDestroyAPIView, AccountView, RetrieveAccountView, UserLoginView

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("accounts/<uuid:pk>/", AccountRetriveUpdateDestroyAPIView.as_view()),
    path("accounts/<uuid:pk>/management/", AccountManagementView.as_view()),
    path("accounts/newest/<int:num>/", RetrieveAccountView.as_view()),
    path("login/", UserLoginView.as_view()),
]
