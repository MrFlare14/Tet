from django import forms
from .models import Post, Cm

class Create_po(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']

class Create_mo(forms.ModelForm):
    class Meta:
        model = Cm
        fields = ['title']
