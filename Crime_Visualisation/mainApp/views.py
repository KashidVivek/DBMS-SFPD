from django.shortcuts import render
from mainApp.models import *


# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')


# def user(request):
#     user_list = .objects.order_by('user_id')
#     user_dict = {'users': user_list}
#     return render(request, 'mainApp/user.html', context=user_dict)


def police_page(request):
    return render(request, 'mainApp/police_page.html')


def register(request):
    return render(request, 'mainApp/register.html')


def user_page(request):
    return render(request, 'mainApp/user_page.html')
