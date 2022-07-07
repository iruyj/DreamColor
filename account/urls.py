from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name ='account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.signup, name='signup'),
    path('mypage/<str:userid>',views.mypage, name='mypage'),
]