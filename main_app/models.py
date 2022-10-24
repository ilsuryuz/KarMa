from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    year = models.IntegerField()
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mark
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})
    