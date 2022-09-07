from django.urls import path
from . import views
urlpatterns = [
    path('', views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
]
