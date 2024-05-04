from rest_framework import serializers

from .models import LookBook, LookBookImage


class LookBookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LookBookImage
        fields = '__all__'

    def to_representation(self, instance):
        return instance.image.url


class LookBookSerializer(serializers.ModelSerializer):
    images = LookBookImageSerializer(many=True)

    class Meta:
        model = LookBook
        fields = '__all__'

