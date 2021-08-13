from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import (ReqistrationSerializer, ActivationSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, LoginSerializer)



class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializers = ReqistrationSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.create(serializers.validated_data)
            return Response('Аккаунт успешно зарегистрован', status=201)





class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Аккаунт успешно активирован', status=status.HTTP_200_OK)




class LoginView(ObtainAuthToken):
    pass


class LogoutView():
    pass

class ChangePasswordView():
    pass



class ForgotPasswordView():
    pass
