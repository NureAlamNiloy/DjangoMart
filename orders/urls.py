from . import views
from django.urls import path

urlpatterns = [
    path('order_complete/', views.order_complete, name ='order_complete'),
]