
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view reponsável, nome refencia
    path('admin/', admin.site.urls),
    
    # usuarios.com
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name="listagem_usuarios")
]
