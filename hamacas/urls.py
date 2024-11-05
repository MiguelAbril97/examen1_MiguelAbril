from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('valoracion/<int:id_hamaca>/', views.ultima_valoracion_hamaca, name='ultima_valoracion_hamaca'),
    path('hamacas/puntuacion/<int:id_usuario>/',views.puntuacion_usuario,name='puntuacion_usuario'),
    path('usuarios/no_valoracion',views.usuarios_no_valoracion,name="usuarios_no_valoracion"),
    path('usuarios/cuenta/<str:nombre>',views.usuarios_cuenta_nombre,name="usuarios_cuenta_nombre"),
    path('usuarios/valoracion/banco',views.usuarios_votos__puntuacion_banco,name="usuarios_votos__puntuacion_banco"),
]