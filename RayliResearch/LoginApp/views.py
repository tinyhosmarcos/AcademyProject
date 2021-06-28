from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView

from .forms import *
from .models import *
#UserCreationForm
from django.contrib.auth.forms import UserCreationForm


class LoginView(View):
	template_name = 'LoginApp/login.html'
	context={

	}
	def get(self, request, *args, **kwargs):
		form 								=IniciarSesionForm(request.POST)
		self.context['form']				=form
		self.context['iniciar_sesion']		=True
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		form = IniciarSesionForm(data=request.POST)
		if form.is_valid():
			# Recuperamos las credenciales validadas
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			# Verificamos las credenciales del usuario
			user = authenticate(username=username, password=password)

			# Si existe un usuario con ese nombre y contraseña
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('RayliApp:inicio')
		self.context['form']				=form
		self.context['iniciar_sesion']		=False
		return render(request, self.template_name,self.context )



class RegisterView(View):
	template_name = 'LoginApp/register.html'
	context={

	}
	def get(self, request, *args, **kwargs):
		form 								=RegistroUsuarioForm(request.POST)
		self.context['form']				=form
		self.context['iniciar_sesion']		=False
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		form = RegistroUsuarioForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			# Si el usuario se crea correctamente 
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('RayliApp:inicio')

			# Si llegamos al final renderizamos el formulario
			return render(request, self.template_name,self.context)


class MisDatosView(View):
	template_name = 'LoginApp/datos.html'
	context={

	}
	def get(self, request, *args, **kwargs):
		user= User.objects.get(id=request.user.id)
		form 								=CambiarDatosForm(instance_user=user)
		self.context['form']				=form
		self.context['user'] 				=user
		self.context['toast']				=False
		return render(request, self.template_name,self.context )

	def post(self, request, *args, **kwargs):
		user= User.objects.get(id=request.user.id)
		form=CambiarDatosForm(data=request.POST)
		if form.is_valid():
			print("pas")
			test=form.save()
			
			user=User.objects.get(id=test)
			update_session_auth_hash(request,user)

			
			# Si el usuario se crea correctamente 
		else:
			print(form.errors)
		user= User.objects.get(id=request.user.id)
		self.context['toast']= True
		form 								=CambiarDatosForm(instance_user=user)
		self.context['form']				=form
		self.context['user'] 				=user
		return render(request, self.template_name,self.context)