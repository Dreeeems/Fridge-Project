from rest_framework import serializers
from .models import Item, Type

class typeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Type
        fields = ['id','name']


class ItemSerializer(serializers.ModelSerializer):
    type = typeSerializer()
    class Meta : 
        model = Item
        fields = ['id','name','type','number','lastDate']
