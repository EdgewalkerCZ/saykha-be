from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag
from testdata.serializers import TagSerializer


TAGS_URL = reverse('testdata:tag-list')


class PublicTagsApiTests(TestCase):
    """ Test the publicly available tags API """

    def SetUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """ Test that login is required """
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """ Test private tags API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@authtestuser.test',
            'password123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """ Test retrieving tags """
        Tag.objects.create(user=self.user, name='EMI')
        Tag.objects.create(user=self.user, name='E2E')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """ Test that tags are returned only for authenticated user"""
        user2 = get_user_model().objects.create_user(
            'test2@authtestuser.test',
            'password123'
        )
        Tag.objects.create(user=user2, name='CAPP')
        tag = Tag.objects.create(user=self.user, name='Vyasu')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)
