from rest_framework import serializers

from .models import Product, ProductSize, ProductImage, ProductColor


class ProductSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSize
        fields = ['size']

    def to_representation(self, instance):
        return instance.size


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['image']

    def to_representation(self, instance):
        return instance.image.url


class ProductColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductColor
        fields = ['color']

    def to_representation(self, instance):
        return instance.color


class ProductSerializer(serializers.ModelSerializer):
    sizes = ProductSizeSerializer(many=True)
    images = ProductImageSerializer(many=True)
    colors = ProductColorSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

