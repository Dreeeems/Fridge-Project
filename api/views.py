from rest_framework import generics
from .models import Item, Type
from .serializers import ItemSerializer, typeSerializer


#Get and Post route  for item
class ItemList(generics.ListCreateAPIView):
        queryset = Item.objects.all()
        serializer_class= ItemSerializer


#Get,Patch and Delete route for item with is pk key 
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer


#Get and Post route  for type

class TypeList(generics.ListCreateAPIView):
        queryset= Type.objects.all()
        serializer_class = typeSerializer

#Get,Patch and Delete route for type with is pk key 
class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Type.objects.all()
        serializer_class = typeSerializer
