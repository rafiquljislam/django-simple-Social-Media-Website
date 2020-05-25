from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.html import format_html


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)


    def imageeeee(self):
        return format_html('<img width="70" height="50" src="/media/%s" />' % self.image)
    
