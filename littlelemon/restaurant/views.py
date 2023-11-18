from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
