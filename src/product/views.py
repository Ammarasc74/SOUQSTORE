from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
# Create your views here. , get_object_or_404
from .models import Product


# class HomeView(ListView):
#     model = Product
#     template_name = "product_list.html"


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 4) 

    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    return render(request,'product/product_list.html',{'product_list':product_list})


def product_detail(request,slug):
    product_detail = Product.objects.get(PRDSLug=slug)

    return render(request,'product/product_detail.html',{'product_detail':product_detail})


def checkout(request):
    return render(request,"checkout.html")

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "product_detail.html"