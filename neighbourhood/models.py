from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.CharField(max_length = 30,null=True)
    first_name = models.CharField(max_length = 30,null=True)
    last_name = models.CharField(max_length = 30, null=True)
    bio = models.TextField(blank=True)
    # Profile_pic = models.ImageField(upload_to='profile/')
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
