from django.shortcuts import render
from urunler.models import Urunler

def index(request):
    top_products = Urunler.objects.order_by('-urun_yayinlanma_tarihi')[:3]
    context = {'top_products': top_products,}
    return render(request, 'index/home.html', context)

def hakkimizda(request):
    context = {'title': 'Hakkımızda'}
    return render(request, 'index/hakkimizda.html', context)