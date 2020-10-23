from rest_framework import  serializers
from .models import Product ,Category,Product_Accessories


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductAccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Accessories
        fields = '__all__'




