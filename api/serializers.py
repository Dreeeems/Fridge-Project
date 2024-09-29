from rest_framework import serializers
from .models import Item, Type
from .image_tracker import get_image_url
class typeSerializer(serializers.ModelSerializer) :
        class Meta:
            model = Type
            fields = ['id','name']


class ItemSerializer(serializers.ModelSerializer):
        type = typeSerializer()
        class Meta : 
            model = Item
            fields = ['id','name','type','number','lastDate','image']
        

        def create(self,validated_data):
              type_data = validated_data.pop('type')
              type_instance, created = Type.objects.get_or_create(**type_data)
              validated_data['image'] = get_image_url(validated_data['name'])
              item = Item.objects.create(type=type_instance, **validated_data)
              return item

        def update(self,instance,validated_data):
            type_data = validated_data.pop('type', None)
            instance.name = validated_data.get('name', instance.name)
            instance.number = validated_data.get('number', instance.number)
            instance.lastDate = validated_data.get('lastDate', instance.lastDate)

            if type_data:
                type_instance = instance.type
                type_instance.name = type_data.get('name',type_instance.name)
                type_instance.save()

            instance.save()
            return instance