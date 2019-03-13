from django.contrib.auth.models import User
from django import forms
from .models import Blog

class UserForm(forms.ModelForm):
    password = forms.CharField(widget =forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['editor', 'pub_date']      
          