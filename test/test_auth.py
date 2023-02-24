from django.contrib.auth.models import User
from django.test import TestCase


class LogInTest(TestCase):
    def setUp(self):

        User.objects.create_user(username='mohamedhamed' , password='passwords')
    def test_login(self):
        # send login data
        userhere = User.objects.filter(username='mohamedhamed')
        self.assertTrue(userhere.exists())
