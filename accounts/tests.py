from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import *
from . import views
from django.contrib.auth.models import User
from kraitcore.models import *

class SimpleTests(SimpleTestCase):

    # homepage test
    def test_homepage_status_code(self):
        response = self.client.get('/', follow=True)
        self.assertEquals(response.status_code, 200, )

    def test_homepage_url_by_name(self):
        response = self.client.get(reverse('homepage'), follow=True)
        self.assertEquals(response.status_code, 200)

    # new project test

    def new_project_test(self):
        render_to_response = self.client.get('new/project/')
        self.assertEquals(render_to_response.status_code)

    def new_project_test_by_name(self):
        render_to_response = self.client.get(reverse('new_project'))
        self.assertEquals(render_to_response.status_code, 200)

    # my-tasks
    def my_tasks_test(self):
        render_to_response = self.client.get('my-tasks/')
        self.assertEquals(render_to_response.status_code, 200)

    # my-tasks
    def get_notifications_test(self):
        render_to_response = self.client.get('get_notifications/')
        self.assertEquals(render_to_response.status_code, 200)

    # notifications
    def notification_handler_test(self):
        render_to_response = self.client.get('notification_handler/')
        self.assertEquals(render_to_response.status_code, 200)

    def allnotifications_test(self):
        render_to_response = self.client.get('project/')
        self.assertEquals(render_to_response.status_code, 200)


class ModelTests(TestCase):

    def New_Project_Case(self):
        user = User.objects.all()[0]
        Project.objects.create(user_id=user.id)

    def Project_detail_test(self):
        projObj = Project.objects.all()[0]
        response = self.client.get('project/'+projObj.id)
        self.assertEquals(response.status_code, 200)

class Signup(SimpleTestCase):
    def test_Signup_code(self):
        response = self.client.get('/accounts/signup/', follow=True)
        self.assertEquals(response.status_code, 200, )

    def test_login_code(self):
        response = self.client.get('/accounts/login/', follow=True)
        self.assertEquals(response.status_code, 200, )

    def test_reset_code(self):
        response = self.client.get('/accounts/reset/', follow=True)
        self.assertEquals(response.status_code, 200, )

