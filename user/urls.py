from django.urls import path
from .views import register,login_view,home,NewProduct,addproduct,Carts

urlpatterns = [
    path('register/', register, name='register'),
    path('login',login_view,name='login'),
    path('home',home,name='home'),
    path('product',NewProduct,name='product'),
    path('addproduct/<int:product_id>/', addproduct, name='addproduct'),
    path('cart',Carts,name='cart')
    
    # other paths
]
