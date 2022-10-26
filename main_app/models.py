from email.policy import default
from operator import truediv
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    year = models.IntegerField()
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo= models.ImageField(null=True, blank=True, default="images/default-post.png")
    def __str__(self):
        return self.mark
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, default="images/default-profile-pic.png")
    bio = models.CharField(max_length=100, null=True, default="Car Enthusiast")
    
    def __str__(self):
        return self.user.username


    

    