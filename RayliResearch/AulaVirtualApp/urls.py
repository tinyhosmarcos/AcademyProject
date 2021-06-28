from django.urls import path

from . import views

app_name='AulaVirtualApp'
urlpatterns = [
    path('inicio',views.InicioView.as_view(), name="inicio"),
]