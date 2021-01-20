from django.urls import path

from authentication.api.views import LoginAPIView, RegistrationAPIView, UserAPIView, UserListAPI, verify_email
from .views import GoogleLogin

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('register/', RegistrationAPIView.as_view(), name="register"),
    path('user/<int:id>/', UserAPIView.as_view(), name="user"),
    path('user/', UserListAPI.as_view(), name="user_list"),
    path('user/verify-email/<uuid:uid>', verify_email, name='verify_email'),
    path('google/', GoogleLogin.as_view(), name="google_oauth")
]
