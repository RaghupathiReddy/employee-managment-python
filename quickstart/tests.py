from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from quickstart.models import Project

User = get_user_model()

PROJECT_DETAILS = {"name": "Test", "description": "Test Project"}
USER_CRED = {"email": "user@test.com", "password": "#1Tester"}
USER_NAME = {"first_name": "User", "last_name": "Test"}


class TestProjectViewSet(APITestCase):
    project_list = reverse("projects-list")

    def setUp(self):
        email = USER_CRED.get("email")
        password = USER_CRED.get("password")
        self.user = User.objects.create_user(email, email, password, **USER_NAME)
        project = Project.objects.create(name='test', description="Test Set Up")
        self.project_detail = reverse("projects-detail", args=[project.pk])
        self.client.login(username=self.user.username, password=password)

    def tearDown(self):
        self.user.delete()

    def test_list(self):
        response = self.client.get(self.project_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        payload = {"name": 'test_project', "description": 'Test project'}
        response = self.client.post(self.project_list, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve(self):
        response = self.client.get(self.project_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update(self):
        payload = {"description": "Test Project 1"}
        response = self.client.patch(self.project_detail, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy(self):
        response = self.client.delete(self.project_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter(self):
        payload = {"name": "Test Project 1"}
        response = self.client.get(self.project_list, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
