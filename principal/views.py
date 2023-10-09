from django.shortcuts import render

def inicio(request):
    titulo = "inicio"
    context={
        "titulo": titulo,
    }
    return render(request, 'index.html', context)