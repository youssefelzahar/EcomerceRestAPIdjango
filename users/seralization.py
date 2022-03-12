from django.db.models.fields import files
from rest_framework import serializers
from .models import*
# from djoser.serializers import UserCreateSerializer, UserSerializer
class Clothesser(serializers.ModelSerializer):

    class Meta:
        model=Clothes
        fields='__all__'
        lookup_field = "title"
     

class Hardser(serializers.ModelSerializer):

    class Meta:
        model=Hardware
        fields='__all__'
        lookup_field = "title"
class Booksser(serializers.ModelSerializer):

    class Meta:
        model=Books
        fields='__all__'
        lookup_field = "title"

# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         models=User
#         files='__all__'