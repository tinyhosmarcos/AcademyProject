from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404

class InicioView(View):
	template_name = 'AulaVirtualApp/inicio.html'
	context={

	}
	def get(self,request,*args,**kwargs):
		
		return render(request, self.template_name,self.context )
	#def post(self,request,*args,**kwargs):