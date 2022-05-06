from django.urls import path,include
from mailapp.views import stdform

urlpatterns=[
    path('',stdform,name='stdform')
   ]