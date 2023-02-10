from rest_framework import serializers
from .models import (Category,
                     Advertisement,
                     Image)


class ADSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class AdvertisementSerializers(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('category', 'user', 'title', 'price', 'description', 'phone', 'create_ad')

    def create(self, validated_data):
        category = validated_data.pop('category')
        advertisement = Advertisement.objects.create(category=category, **validated_data)
        return advertisement


class ImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image',  'ad')