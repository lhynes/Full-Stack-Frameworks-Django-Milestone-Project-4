from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_adventures, name='adventures'),
    path('<int:adventure_id>/', views.adventure_detail, name='adventure_detail'),
    path('add/', views.add_adventure_package, name='add_adventure_package'),
]