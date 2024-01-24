from rest_framework import serializers

from bizz.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"