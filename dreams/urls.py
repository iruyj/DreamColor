from django.contrib import admin
from django.urls import path, include

from dreams import views

app_name = 'dream'

urlpatterns = [
    path('create/', views.createDream, name='create' ),
    path('', views.mainPage, name='main'),

    path('color/<str:color_id>', views.search_color, name='color'),
    path('title/', views.search_title, name='title'),
    path('modify/<int:id>', views.modify, name='modify'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('<int:id>', views.viewDream, name='detail'),
    path('read/<int:id>', views.read_count, name='read_cnt'),
    path('search/', views.search, name='search'),

]
