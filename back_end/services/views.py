from django.shortcuts import render
from rest_framework import generics

from .models import Request
from .serializers import RequestSerializer,SectorSerializer

class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class SectorListView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = SectorSerializer