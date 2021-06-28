from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import *
class InicioView(View):
	template_name = 'RayliApp/inicio.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		ListServicios=Servicio.objects.all()
		ListCursos=Curso.objects.all()
		self.context['ListServicios']= ListServicios
		self.context['ListCursos']=ListCursos
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):
	
class NosotrosView(View):
	template_name = 'RayliApp/nosotros.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):	

class TiendaView(View):
	template_name = 'RayliApp/tienda.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):	


class ServiciosView(View):
	template_name = 'RayliApp/servicios.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):	

class DetalleServicioView(View):
	template_name = 'RayliApp/detalle_servicio.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		servicio=get_object_or_404(Servicio,pk=kwargs['servicio_id'])
		self.context['servicio']=servicio
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):	
	



class ContactoView(View):
	template_name = 'RayliApp/contacto.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):	


class CapacitacionView(View):
	template_name = 'RayliApp/capacitacion.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):	

class CursoView(View):
	template_name = 'RayliApp/curso.html'
	context={

	}
	def get(self,request,*args, **kwargs):
		curso 			= get_object_or_404(Curso,pk=kwargs['curso_id'])
		self.context['curso']	= curso

		return render(request,self.template_name,self.context )




class AprendeView(View):
	login_required = True
	template_name = 'RayliApp/aprende.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):	

