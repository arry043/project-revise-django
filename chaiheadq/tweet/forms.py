from django import forms
from .models import Tweet

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
