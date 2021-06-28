from django.urls import path

from django.contrib.auth.decorators import login_required
from . import views

app_name='RayliApp'
urlpatterns = [
    path('inicio', views.InicioView.as_view(),                   name='inicio'),
    path('nosotros', views.NosotrosView.as_view(),               name='nosotros'),
    path('servicios', views.ServiciosView.as_view(),             name='servicios'),
    path('servicios/<int:servicio_id>/',views.DetalleServicioView.as_view(),name='detalle_servicio'),
    path('tienda', views.TiendaView.as_view(),                   name='tienda'),
    path('contacto', views.ContactoView.as_view(),               name='contacto'),
    path('capacitacion', views.CapacitacionView.as_view(),       name='capacitacion'),
    path('capacitacion/<int:curso_id>/',views.CursoView.as_view(),name='curso'),
    path('aprende', login_required(views.AprendeView.as_view()),  name='aprende'),
]