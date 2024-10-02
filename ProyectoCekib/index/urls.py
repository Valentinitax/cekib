from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta de la página principal
    path('nosotros/', views.nosotros, name='nosotros'),  # Página "¿Quiénes Somos?"
    path('servicios/', views.servicios, name='servicios'),  # Página de servicios
    path('blog/', views.blog, name='blog'),  # Página del blog
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
]
