from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user_id = models.CharField(max_length = 30,null=True)
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
def Create_user_profile(sender,instance,created, **kwargs):
    if created:
        profile.objects.created(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance, **kwargs):
    insatnce.profile.save()

class Hood(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'pics',null = True)
    admin = models.ForeignKey(Profile, related_name = 'hoods', null=True)
    description = models.CharField(max_length = 300, default = 'My hood')

class Business(models.Model):
    name = models.CharField(max_length = 30)
    cartefory = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 10)
    image = models.ImageField(upload_to = 'Businessimage/')
    description = models.CharField(max_length = 200)
    profile = models.ForeignKey(Profile, related_name = 'profiles')

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

        
