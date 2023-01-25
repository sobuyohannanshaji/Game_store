from django.forms import ModelForm
from .models import *
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(),max_length=100)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    class Meta:
        model=Userone
        fields=['name','email','username','gender','password']

class UserForm1(ModelForm):
    class Meta:
        model=Userone
        fields=['name','email','gender','username']

class UserForm2(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    class Meta:
        model=Userone
        fields=['password']

# class GameForm(forms.ModelForm):
#     game_avatar=forms.ImageField()
#     game_images = forms.ImageField()
#     game_video1 = forms.FileField()
#     game_video2=forms.FileField()
#     game_file = forms.FileField()
#     game_name=forms.CharField(max_length=100)
#     game_type = forms.ChoiceField( choices=(('free','free'),('paid','paid'),),widget=forms.Select(),required=True)
#     game_amt = forms.CharField(max_length=100)
#
#     class Meta:
#         model=game_details
#         fields=['game_name','game_avatar','game_images','game_video1','game_video2','game_file','game_type','game_amt']
#
#
