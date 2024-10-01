from django.shortcuts import render
from rest_framework import generics
from .models import Order, Batch
from .serializers import OrderSerializer, BatchSerializer

class OrderAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BatchAPIView(generics.ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
