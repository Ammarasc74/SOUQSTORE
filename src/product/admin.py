from django.contrib import admin
from .models import Product ,ProductOrder,Order, ProductImage ,Category ,Product_Alternative , Product_Accessories


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
admin.site.register(ProductOrder)
admin.site.register(Order)
