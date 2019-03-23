from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30,null=True)
    last_name = models.CharField(max_length = 30, null=True)
