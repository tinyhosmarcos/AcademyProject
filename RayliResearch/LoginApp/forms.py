from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.forms.widgets import PasswordInput, TextInput
class IniciarSesionForm(AuthenticationForm):
	username = forms.CharField(widget=TextInput(attrs={'class':'validate'}))
	password = forms.CharField(widget=PasswordInput(attrs={'class':'validate'}))
	class Meta:
		model = User		



class RegistroUsuarioForm(UserCreationForm):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=14,widget=TextInput(attrs={'class':'validate',}),help_text='asdasd')
	first_name = forms.CharField(max_length=120)
	last_name = forms.CharField(max_length=120)
	email = forms.EmailField(max_length=264)
	
	class Meta:
		model = User
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)


class CambiarDatosForm(forms.Form):
	username_old=forms.CharField(max_length=32,widget=forms.TextInput(attrs={'class':'input ', 'style':'display:none' ,'type':'hidden'}))
	username=forms.CharField(max_length=32)
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	email = forms.EmailField(max_length=64)

	class Meta:
		model = User
		# I've tried both of these 'fields' declaration, result is the same
		# fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
		fields =['username_old','username','first_name', 'last_name', 'email']
		

	def __init__(self,*args,**kwargs):
		user=kwargs.pop('instance_user',None)
		super(CambiarDatosForm, self).__init__(*args, **kwargs)
		if user:
			self.fields['username_old'].initial	=user.username
			self.fields['username'].initial		=user.username
			self.fields['first_name'].initial	=user.first_name
			self.fields['last_name'].initial	=user.last_name
			self.fields['email'].initial		=user.email

	def clean(self):
		cleaned_data=super().clean()
		
		validate_username=User.objects.filter(username=self.cleaned_data['username'])

		if validate_username and self.cleaned_data['username']!=self.cleaned_data['username_old']:
			raise ValidationError({'username': ["Nombre de Usuario no disponible",]})
		print(cleaned_data.get('username_old'))
		return self.cleaned_data   			

	def save(self, commit=True):
		user=None	
		if self.cleaned_data['username']!=self.cleaned_data['username_old']:
			user 	= User.objects.filter(username=self.cleaned_data['username_old']).update(
			username=self.cleaned_data['username'],
			first_name=self.cleaned_data['first_name'],
			last_name=self.cleaned_data['last_name'],
			email=self.cleaned_data['email'],
			)
		
		if self.cleaned_data['username']==self.cleaned_data['username_old']:
			user 	= User.objects.filter(username=self.cleaned_data['username_old']).update(
			first_name=self.cleaned_data['first_name'],
			last_name=self.cleaned_data['last_name'],
			email=self.cleaned_data['email'],
			)
		return user