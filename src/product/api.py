from .models import Product , Category,Product_Accessories
from .serializers import ProductSerializer ,CategorySerializer,ProductAccessoriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
# from rest_auth.registration.views import SocialLoginView
# from rest_auth.social_serializers import TwitterLoginSerializer
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
# from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from rest_auth.registration.views import SocialConnectView
# from rest_auth.social_serializers import TwitterConnectSerializer


# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter

# class TwitterLogin(SocialLoginView):
#     serializer_class = TwitterLoginSerializer
#     adapter_class = TwitterOAuthAdapter


class Product_List_Api(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer



class Product_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    lookup_field = 'slug'


class Category_List_Api(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer


class Category_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer
    lookup_field = 'slug'

class Accessories_List_Api(generics.ListCreateAPIView):
    queryset = Product_Accessories.objects.all()
    serializer_class =  ProductAccessoriesSerializer


class Accessories_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_Accessories.objects.all()
    serializer_class =  ProductAccessoriesSerializer
    lookup_field = 'slug'