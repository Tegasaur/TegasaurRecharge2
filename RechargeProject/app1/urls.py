from django.contrib import admin
from django.urls import path
from app1 import views
app_name='app1'
urlpatterns = [
    path('', views.RechargeCardV.index, name='index'),
    path('purchase/', views.RechargeCardV.purchase, name='purchase'),
    path('payment/', views.RechargeCardV.payment, name='payment'),
    path('show/', views.RechargeCardV.show, name='show'),
    path('about/', views.RechargeCardV.about, name='about')
]
