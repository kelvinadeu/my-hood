from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user_id = models.OneToOneField(User, max_length = 30,null=True)
    first_name = models.CharField(max_length = 30,null=True)
    last_name = models.CharField(max_length = 30, null=True)
    bio = models.TextField(blank=True)
    # Profile_photo = models.ImageField(upload_to='pics/')
    # hood = models.ForeignKey('Hood', blank=True, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user_id = instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance, **kwargs):
        instance.profile.save()

class Hood(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'pics',null = True)
    # admin = models.ForeignKey(Profile, related_name = 'hoods', null=True)
    population = models.CharField(max_length = 300, default = 'My hood')

class Business(models.Model):
    name = models.CharField(max_length = 30)
    cartegory = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 10)
    image = models.ImageField(upload_to = 'Businessimage',null=True)
    description = models.CharField(max_length = 200)
    # profile = models.ForeignKey(Profile, related_name = 'profiles')


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def __str__(self):
        return self.name

    @classmethod
    def search_by_name(cls,search_term):
        business = cls.objects.filter(title__icontains=search_term)
        return business

class Post(models.Model):
    user_id = models.ForeignKey(User)
    post = models.CharField(max_length = 40)


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.post

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location

class Cartegory(models.Model):
    name = models.CharField(max_length = 30)

    def save_cartegory(self):
         self.save()

    def delete_cartegory(self):
        self.delete()

    def __str__ (self):
        return self.cartegory
