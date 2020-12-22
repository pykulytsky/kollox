from django.urls import path

from authentication.api.views import LoginAPIView, RegistrationAPIView, UserAPIView, UserListAPI

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('register/', RegistrationAPIView.as_view(), name="register"),
    path('user/<int:id>/' ,UserAPIView.as_view(), name="user"),
    path('user/', UserListAPI.as_view(), name="user_list")
]
