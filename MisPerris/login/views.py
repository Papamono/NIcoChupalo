from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios, Mascotas


# Create your views here.
def mostrarInicio(request):
    return render(request, 'inicio.html', {})

def mostrarLogin(request):
    return render(request, 'login.html', {})

def mostrarSignUp(request):
    return render(request, 'signup.html', {})

def mostrarRegistro(request):
    return render(request, 'registro.html', {})

def mostarListado(request):
    return render(request, 'listado.html', {'Listado_registro' : Mascotas.objects.all()})

def mostrarModificar(request):
    id_mascota = request.POST.get('idMascota', '')
    mascota = Mascotas.objects.get(pk = id_mascota)
    return render(request, 'modificar.html', {'mascota': mascota})

def crearUsuario(request):
    nombre_usuario = request.POST.get('nombreUsuario', 'vacio')
    clave = request.POST.get('clave', 'vacio')
    correo = request.POST.get('correo', 'vacio')

    usuario = Usuarios(nombre_usuario = nombre_usuario, clave = clave, correo = correo)
    usuario.save()

    return render(request, 'inicio.html', {})

def crearMascota(request):

    fotografia = request.POST.get('fotografia', False)
    nombre_mascota = request.POST.get('nombreMascota', '')
    raza_predominante = request.POST.get('razaPredominante', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', '')

    mascota = Mascotas(fotografia = fotografia, nombre_mascota = nombre_mascota, raza_predominante = raza_predominante, descripcion = descripcion,
                       estado =estado)

    mascota.save()

    return render(request, 'inicio.html', {})

def modificarMascota(request):

    id_mascota = request.POST.get('modificarIdMascota', '')
    mascota = Mascotas.objects.get(pk = id_mascota)

    fotografia = request.POST.get('modificarFotografia', False)
    nombre_mascota = request.POST.get('modificarNombreMascota', '')
    raza_predominante = request.POST.get('modificarRazaPredominante', '')
    descripcion = request.POST.get('modificarDescripcion', '')
    estado = request.POST.get('modifcarEstado', '')

    mascota.fotografia = fotografia
    mascota.nombre_mascota = nombre_mascota
    mascota.raza_predominante = raza_predominante
    mascota.descripcion = descripcion
    mascota.estado = estado

    mascota.save()

    return render(request, 'inicio.html', {})

def eliminarMascota(request):

    id_mascota = request.POST.get('eliminarIdMascota', '')
    mascota = Mascotas.objects.get(pk = id_mascota)

    mascota.delete()

    return render(request, 'inicio.html', {})

def verificarLogin(request):
    return render(request, 'inicio.html', {})
