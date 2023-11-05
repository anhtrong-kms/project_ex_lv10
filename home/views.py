from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {
        "products": products,
        "categorys" : categorys,
    }
    return render(request, 'home/home.html', context)

def categoryCLB(request):
    category = request.GET.get('category','')
    product_category = Product.objects.filter(Category__name = category)
    context = {
        'product_category': product_category
    }
    return render(request, 'home/category_CLB.html', context)