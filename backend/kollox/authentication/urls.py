from django.urls import path

from authentication.api.views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('register/', RegistrationAPIView.as_view(), name="register")
]
