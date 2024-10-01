from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
