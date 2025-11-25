# payments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.initiate_payment, name='initiate_payment'),
    path('success/', views.success, name='success'),
    path('fail/', views.fail, name='fail'),
    path('cancel/', views.cancel, name='cancel'),
]