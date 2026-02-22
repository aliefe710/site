from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-home'),
    path('hakkimizda/', views.hakkimizda, name='index-hakkimizda'),
]