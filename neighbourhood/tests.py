from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


# Create your tests here.
class UserProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = UserProfile(id=1,first_name='Firstname',last_name='Lastname',user=self.new_user,location='Test Location')

def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))
