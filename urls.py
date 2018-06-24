from django.conf.urls import  url
from django.urls import path
from . import views
urlpatterns = [

    url(r'^index', views.index),
    url(r'^login', views.login),
    url(r'^home', views.home),
    url(r'^register', views.register),
    url(r'^Hindipoem',views.hindipoem),
    url(r'^AddPoem',views.AddPoem),
    url(r'^logout',views.logout),
    url(r'^mail',views.mail),

]