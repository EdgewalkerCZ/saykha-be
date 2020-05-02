from django.shortcuts import render
from .models import UserData

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from testdata import serializers


def index(request):
    """This is index for testdata,
    can be later switched to testportal app module"""
    user_data_list = UserData.objects.all().order_by('environment')
    context = {'user_data_list': user_data_list}

    return render(request, 'index.html', context)


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """ Manage Tags in the database """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """ Return objects for the current authenticated user only """
        return self.queryset.filter(user=self.request.user).order_by('-name')
