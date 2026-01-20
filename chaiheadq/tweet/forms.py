from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'What’s happening, Arry? 😎'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        