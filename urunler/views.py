from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Urunler
# Create your views here.

def index(request):
    # return all products ordered by publish date (newest first)
    latest_urunler_list = Urunler.objects.order_by("-urun_yayinlanma_tarihi")

    context = {"latest_urunler_list": latest_urunler_list,}

    return render(request, "urunler/index.html", context)


def detail(request, urunler_id):
    try:
        urun = Urunler.objects.get(pk=urunler_id)
    except Urunler.DoesNotExist:
        raise Http404("Urun bulunamadi.")
    return render(request, "urunler/detail.html", {"urun": urun})