from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationsSerializer


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationsSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.create(user=account)
            data['response'] = 'successfully registered a new user'
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)