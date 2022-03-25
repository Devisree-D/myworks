"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Fruits.views import fruit_create,fruit_view,fruit_delete,fruit_update,registration,login_view,log_out
from Fruits.views import Fruits,FruitDetail,FruitUpdate,Fruitcreate,Fruitdelete
urlpatterns = [
    path('create/',fruit_create,name="create"),
    path('delete/<int:id>',fruit_delete,name="delete"),
    path('view/<int:id>',fruit_view,name="view"),
    path('update/<int:id>',fruit_update,name="update"),
    path('register/',registration,name="register"),
    path('login/',login_view,name="login"),
    path('logout/',log_out,name="out"),
    path('clslist/',Fruits.as_view(),name="clslist"),
    path("clscreate/",Fruitcreate.as_view(),name="clscreate"),
    path('clsupdate/<int:pk>',FruitUpdate.as_view(),name="clsupdate"),
    path('clsdetail/<int:pk>',FruitDetail.as_view(),name="clsdetail"),
    path('clsdelete/<int:pk>',Fruitdelete.as_view(),name="clsdelete")





]



