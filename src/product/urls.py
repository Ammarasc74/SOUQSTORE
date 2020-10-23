from django.urls import path , include
from . import api
# from . import views
app_name = 'product'


urlpatterns = [
   # # Api
   # path('rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
   # path('rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
   # path('rest-auth/facebook/connect/$', FacebookConnect.as_view(), name='fb_connect'),
   # path('rest-auth/twitter/connect/$', TwitterConnect.as_view(), name='twitter_connect'),
   path('api/product',api.Product_List_Api.as_view(), name='Product_List_Api'),
   path('api/product/<str:slug>',api.Product_Detail_Api.as_view(), name='Product_Detail_Api'),
   path('api/category',api.Category_List_Api.as_view(), name='Category_List_Api'),
   path('api/category/<str:slug>',api.Category_Detail_Api.as_view(), name='Category_Detail_Api'),
   path('api/Accessories',api.Accessories_List_Api.as_view(), name='Accessories_List_Api'),
   path('api/Accessories/<str:slug>',api.Accessories_Detail_Api.as_view(), name='Accessories_Detail_Api'),

]






#    # path('',HomeView.as_view(),name='home' ),
   # path('',views.product_list ),
   # path('profile/<str:slug>', views.product_detail , name='product_detail'),