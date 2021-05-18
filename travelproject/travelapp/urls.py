from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')


]