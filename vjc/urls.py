from django.urls import path
from .views import *

urlpatterns=[
    path('', home, name ="web_home"),
    path('about/', about, name ="web_about"),
   
]
