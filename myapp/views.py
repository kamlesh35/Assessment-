from django.shortcuts import render
from rest_framework import generics
from myapp.serializers import *
from myapp.models import *

# Create your views here.


class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailCreateAPIView(generics.CreateAPIView):
    serializer_class = InvoiceDetailSerializer



