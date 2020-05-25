from .models import Post
from django.forms import *
from django import forms

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','image','content']        
        labels = {
            "title": '',
            "image": '',
            "content": '',
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write a Title'}),
            'content':forms.Textarea(attrs={'class':'form-control','height': '133px','placeholder':'Write Content'}),
        }