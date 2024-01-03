from django.shortcuts import render
from rest_framework import generics
from .models import Demonstrate
from .serializers import DemonstrateSerializer
# Create your views here.


class DemonstrateList(generics.ListCreateAPIView):
	queryset=Demonstrate.objects.all()
	serializer_class=DemonstrateSerializer

class DemonstrateDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Demonstrate
	serializer_class=DemonstrateSerializer

