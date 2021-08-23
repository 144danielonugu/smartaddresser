from django.contrib import admin
from django.urls import path
from addressapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login",views.login,name="login"),
    path("addresslist",views.addresslist,name="addresslist"),
    path("address/<id>",views.addressmain,name="detail"),
    path("logout",views.logout)
]