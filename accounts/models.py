from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    date_joined=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username