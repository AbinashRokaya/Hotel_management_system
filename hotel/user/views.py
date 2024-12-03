from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .serializer import RegisterSerializer,LoginSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

@api_view(['POST'])
def lagout_view(request):
    try:
        if request.method == 'POST':
            refresh_token=request.data.get('refresh_token')
            token=RefreshToken(refresh_token)
            token.blacklist()

        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def registeation_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['username']=account.username
            data['email']=account.email
            # token=Token.objects.get(user=account).key
            # data['token']=token

            refresh = RefreshToken.for_user(account)
            data['token']={
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            }
        else:
            data=serializer.errors
        return Response(data)
    
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to login
def login_view(request):
    if request.method == 'POST':
        serializer=LoginSerializer(data=request.data)

        if serializer.is_valid():
            # Generate JWT tokens
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            data = {
                'username': user.username,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)