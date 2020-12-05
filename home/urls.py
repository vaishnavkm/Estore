from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('',views.home,name='home'),
    path('product-detail',views.product_detail,name='product-detail'),
    path('product-list',views.product_list,name="product-list"),
    path('contact',views.contact,name='contact'),
    path('register',views.register_id,name='register'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('login',views.login_id,name='login'),
    path('logout/',views.logout_user,name='logout'),



]
