
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name = 'cart'),
    path('<int:product_id>', views.AddToCart, name='add_cart'),
    path('remove/<int:product_id>', views.removeCartItem, name = 'remove_cart'),
    path('delete/<int:product_id>', views.removeCart, name = 'delete_cart'),
    path('checkout', views.checkOut, name = 'checkout'),
]