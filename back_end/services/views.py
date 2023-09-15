from django.shortcuts import render
from rest_framework import generics

from .models import Request,Sector
from .serializers import RequestSerializer,SectorSerializer
from rest_framework.permissions import IsAuthenticated





class RequestCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class SectorListView(generics.ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer