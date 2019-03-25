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

def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) > 0)

def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) == 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_business = Business(id = 1,name='Test Business',owner=self.new_user,business_location='Test Location',email='business@email.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))
    
