from django.shortcuts import render

from rest_framework import viewsets, permissions
from apps.posts.models import Post
from .serializer import PostSerializers

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
