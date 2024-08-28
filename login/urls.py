from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página principal de la app
    path('salir', views.salir, name='salir'),  # Ruta para salir de la aplicación
    path('registro', views.registrar, name='registro'),
    path('signin', views.signin, name='signin'),
]