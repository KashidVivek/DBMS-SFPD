from mainApp import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register_page'),
    path('police_page/', views.police_page, name='police_page'),
    path('', views.index, name='index'),
    # path('user/', views.user, name='user'),
    path('user_page/', views.user_page, name='user_page')
]
