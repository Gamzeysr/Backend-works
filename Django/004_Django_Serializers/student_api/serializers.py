from rest_framework import serializers
from .models import Student

#! Bunlar ilkel method👇

class StudentSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    number = serializers.IntegerField()
    age = serializers.IntegerField()

#? Bu yukarıdaki serializers ı yazarsam asagıdaki iki methodu yazmak zorundayım 👇


def create(self, validated_data):
        return Student.objects.create(**validated_data)


def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

        #! ilkel method buraya kadar👆
    #*✨✨2.adım artık serializers ım hazır ben artık view.py e gidip serializers ımı import edebilirim.