from django.forms import ModelForm
from .models import *

from django.forms import DateInput

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

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','bio','photo']