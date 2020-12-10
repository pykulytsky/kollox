from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from authentication.api.serializers import LoginSerializer, RegistrationSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'token': serializer.data.get('token', None)
        })

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




@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def verify_email(request, verification_code):
    # logger.warning(f"{request.META['HTTP_AUTHORIZATION']=}")
    if 'Bearer' in request.META['HTTP_AUTHORIZATION']:
         pass
    else:
        request.META['HTTP_AUTHORIZATION'] = 'Bearer ' + request.session['token']
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