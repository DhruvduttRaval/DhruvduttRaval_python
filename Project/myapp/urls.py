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
]