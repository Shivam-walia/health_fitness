
from django import forms
from models import usermodel

class signupform(forms.ModelForm):
	class Meta:
		model=usermodel
		fields=['username','password','email','contact']
class loginform(forms.ModelForm):
	class Meta:
		model=usermodel
		fields=['username','password']
