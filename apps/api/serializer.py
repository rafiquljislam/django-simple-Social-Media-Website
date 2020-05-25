from rest_framework import serializers
from apps.posts.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','url','title','image','author','content')