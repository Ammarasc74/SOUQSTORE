from django.urls import  path
from . import views
from .views import checkout ,product_list,product_detail
# HomeView,ProductDetailView,
app_name = 'product'


urlpatterns = [
   # path('',HomeView.as_view(),name='home' ),
   path('',views.product_list ),
   path('profile/<str:slug>', views.product_detail , name='product_detail'),
]