from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from authentication.api.serializers import \
    (LoginSerializer,
     RegistrationSerializer,
     UserSerializer,
     UserDetailSerializer)

from rest_framework import generics


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'token': serializer.data.get('token', None),
            'id': serializer.data.get('id', None)
        },
        status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response({
            'info': 'for registration push POST request with "email", "username","password" body fields.'
        })


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()


class UserAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserDetailSerializer

    def get(self, request, id):
        _user = User.objects.get(id=id)

        serializer = self.serializer_class(_user, context={"request": request})
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def patch(self, request, id):
        _user = User.objects.get(id=id)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def verify_email(request, verification_code):

    if not request.user.is_authenticated:
        return Response({
            'status': 'Authenticate first to verify email.'
        })
    else:
        user = request.user
        if user.email_verified == True:
            return Response({
                'status': 'Email allready verified.'
            },
            status=status.HTTP_304_NOT_MODIFIED)

        if user.email_verification_code == verification_code:
            user.email_verified = True
            return Response({
                'status': 'OK'
            },
            status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'Wrong verification code.'
            })