from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'subcategories', 'parent']

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['subcategories'] = CategorySerializer(many=True)
        return fields

