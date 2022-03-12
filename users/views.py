from django.shortcuts import render

from users.seralization import Booksser, Clothesser, Hardser
from .models import*
from rest_framework import viewsets

# Create your views here.



class Clothestable(viewsets.ModelViewSet):
   queryset = Clothes.objects.all()
   serializer_class=Clothesser
   lookup_field = "title"


class Hardwaretable(viewsets.ModelViewSet):
   queryset = Hardware.objects.all()
   serializer_class=Hardser
   lookup_field = "title"

   
class Bookstable(viewsets.ModelViewSet):
   queryset = Books.objects.all()
   serializer_class=Booksser
   lookup_field = "title"