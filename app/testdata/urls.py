from django.urls import path, include

from rest_framework.routers import DefaultRouter
from testdata import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'testdata'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/testdata/', include(router.urls)),
]
