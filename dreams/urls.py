from django.contrib import admin
from django.urls import path, include

from dreams import views

app_name = 'dream'

urlpatterns = [
    path('create/', views.createDream, name='create' ),
    path('', views.mainPage, name='main'),
    path('search', views.findKey, name='search'),
    path('<int:id>', views.viewDream, name='detail'),
]
