from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='urunler-index'),
    path('<int:urunler_id>/', views.detail, name='urunler-detail'),
]