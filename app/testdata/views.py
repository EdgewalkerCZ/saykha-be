from django.shortcuts import render
from .models import UserData


def index(request):
    """This is index for testdata,
    can be later switched to testportal app module"""
    user_data_list = UserData.objects.all().order_by('environment')

    context = {'user_data_list': user_data_list}

    return render(request, 'index.html', context)
