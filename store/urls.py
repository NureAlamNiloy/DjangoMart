from . import views
from django.urls import path

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='product_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.product_details, name='product_details'),
]