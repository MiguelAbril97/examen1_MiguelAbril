from django.shortcuts import render
from .models import *
from django.db.models import Q,F,Prefetch
# Create your views here.

def index(request):
    return render(request, 'index.html') 

def ultima_valoracion_hamaca (request, id_hamaca):
    hamaca=Hamaca.objects.get(id=id_hamaca)
    valoracion = Valoracion.objects.prefetch_related('hamaca','usuario').filter(
        hamaca__id=id_hamaca).order_by('-fecha_valoracion')[:1].get()
    return render(request,'valoracion.html',{'valoracion_mostrar':valoracion, 'hamaca':hamaca})

#uso lt porque es menor a 3, lte es menor o igual a 3. Para mi, menor a 3 excluye al 3

def puntuacion_usuario(request,id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    hamacas = Hamaca.objects.filter(valoracion__valor__lt=3, valoracion__usuario=id_usuario).all()
    return render(request,'hamacas/lista.html',{'hamacas_mostrar':hamacas,'usuario':usuario})  

def usuarios_no_valoracion (request):
    usuarios = Usuario.objects.prefetch_related('voto')
    usuarios = usuarios.filter(valoracion=None)
    return render(request,'usuarios.html' ,{'usuarios_mostrar':usuarios})

def usuarios_cuenta_nombre (request, nombre):
    usuarios = Banco.objects.select_related('usuario').filter(
        Q(banco = 'UNI') | Q(banco = 'CAI'), usuario__nombre__contains =nombre).all()
    return render(request,'banco/usuarios.html' ,{'usuarios_mostrar':usuarios})

#Exclude descartara todos los usuarios que no esten en la tabla banco
def usuarios_votos__puntuacion_banco(request):
    usuarios = Valoracion.objects.prefetch_related('usuario').filter(
        fecha_valoracion__year__gte=2023, valor=5).exclude(usuario__banco=None)
    return render (request, 'usuarios.html',{'usuarios_mostrar' : usuarios})

#Errores
def mi_error_400(request, exception=None):
    return render(request, 'errores/400.html', None, None, 400)

def mi_error_403(request, exception=None):
    return render(request, 'errores/403.html', None, None, 403)

def mi_error_404(request, exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def mi_error_500(request):
    return render(request, 'errores/500.html', None, None, 500)
