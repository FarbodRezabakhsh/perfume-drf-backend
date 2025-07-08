from rest_framework import serializers
from .models import Category, Label, Brand

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ["id", "name", "slug", "parent", "is_active"]


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Label
        fields = ["id", "name", "color", "is_active"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Brand
        fields = ["id", "name", "logo", "description", "is_active"]
