from typing import Text
from django import forms
from django.db.models import fields
#from django import forms
#from .models import User
from home.models import Photo

class PhotoForm(forms.ModelForm):
  class Meta:
   model = Photo
   fields = '__all__'
   labels = {'photo':''}
  