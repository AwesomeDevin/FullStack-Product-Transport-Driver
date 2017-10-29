from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from rest_framework import viewsets, status
from serializers import *
from models import *
import json

class UserViewSet(viewsets.ModelViewSet):
    """
    TaskInfoSet表的增删改查
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

