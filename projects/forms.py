from django.forms import ModelForm
from .models import *
from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User

class TaskForm(ModelForm):
  class Meta:
      model =Task
      fields ='__all__'
      widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
               attrs={'type': 'date' }),
               }

class ProjectForm(ModelForm):
  class Meta:
      model =Project
      fields ='__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'position', 'email', 'photo', 'bio']
        widgets = {
            'user': forms.HiddenInput(),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'value': 'world98765'}, render_value=True),
        }