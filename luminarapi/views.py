from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from luminarapi.serializers import UserSerializer

class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    model=User
    http_method_names=["post","get"]


