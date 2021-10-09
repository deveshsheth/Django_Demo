from django.forms import ModelForm 
from .models import *


class bookmodelform(ModelForm):
	class Meta:
		model = bookmodel
		fields = '__all__'

class signupmodelform(ModelForm):
	class Meta:
    	 model = signupmodel
    	 fields = '__all__'
