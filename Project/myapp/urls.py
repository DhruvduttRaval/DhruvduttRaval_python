from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('products/',views.products,name='products'),
    path('checkout/',views.checkout,name='checkout'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('new_password/',views.new_password,name='new_password'),
    path('profile/',views.profile,name='profile'),
    path('seller_change_password/',views.seller_change_password,name='seller_change_password'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_view_products/',views.seller_view_products,name='seller_view_products'),

]