from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def blog(request):
    return render(request, 'blog.html')

def contacto(request):
    return render(request, 'contacto.html')