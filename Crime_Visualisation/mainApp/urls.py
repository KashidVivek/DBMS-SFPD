from mainApp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
]
