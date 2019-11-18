from django.shortcuts import render
from mainApp.models import portalUser


# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')


def user(request):
    user_list = portalUser.objects.order_by('user_id')
    user_dict = {'users': user_list}
    return render(request, 'mainApp/user.html', context=user_dict)
