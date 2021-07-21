from django import forms
from home.models import Stock
#from home.models import Feedback
#renuka file
from home.models import Photo

class PhotoForm(forms.ModelForm):
  class Meta:
   model = Photo
   fields = '__all__'
   labels = {'photo':''}
  

Star=[
    ('rate5', 'rate-5'),
    ('rate4', 'rate-4'),
    ('rate3', 'rate-3'),
    ('rate2', 'rate-2'),
    ('rate1', 'rate-1')
]
class Stockform(forms.ModelForm):
    class Meta:
        model = Stock
        fields= '__all__'

#class Feedbackform(forms.ModelForm):
    #name=forms.CharField(max_length=20)
    #starrating=forms.CharField(widget=forms.RadioSelect(choices=Star))
    #suggestion=forms.CharField(max_length=100)
    #class Meta:
        #model = Feedback
        #fields= ['name', 'starrating','suggestion']

