from django.urls import  path
from . import views

app_name = 'product'


urlpatterns = [
   path('',views.product_list ),
   path('profile/<str:slug>', views.product_detail , name='product_detail'),
]