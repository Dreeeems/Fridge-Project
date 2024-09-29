from rest_framework import serializers
from .models import Item, Type

class typeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Type
        fields = ['id','name']
