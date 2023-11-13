from django.shortcuts import render

def inicio(request):
    titulo = "inicio"
    context={
        "titulo": titulo,
    }
    return render(request, 'index.html', context)

def login(request):
    titulo = "inicio de Sesion"
    context={
        "titulo": titulo,
    }
    return render(request, 'login.html', context)