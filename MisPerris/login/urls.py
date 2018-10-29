from django.urls import path
from . import views

urlpatterns = [
    path('inicio/' , views.mostrarInicio, name = "mostrarInicio"),
    path('inicio/login/' , views.mostrarLogin, name = "mostrarLogin"),
    path('inicio/signup/' , views.mostrarSignUp, name = "mostrarSignUp"),
    path('inicio/signup/crearUsuario/', views.crearUsuario, name = "crearUsuario"),
    path('inicio/registro/', views.mostrarRegistro, name = "mostrarRegistro"),
    path('inicio/registro/crearRegistro/', views.crearMascota, name= "crearMascota"),
    path('inicio/listar/', views.mostarListado, name = "mostarListado"),
    path('inicio/modificar/', views.mostrarModificar, name = "modificarMascota"),
    path('inicio/modificar/modificarRegistro/', views.modificarMascota, name = "modificarMascota"),
    path('inicio/modificar/eliminarRegistro/', views.eliminarMascota, name = "elimnarMascota"),
]
