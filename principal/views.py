from django.shortcuts import render

def inicio(request):
    titulo = "inicio"
    context={
        "titulo": titulo,
    }
    return render(request, 'index.html', context)

def login(request):
    titulo = "Selecciona tu Rol"
    context={
        "titulo": titulo,
    }
    return render(request, 'login.html', context)