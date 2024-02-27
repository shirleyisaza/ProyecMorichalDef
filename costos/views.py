from django.shortcuts import render

# Create your views here.


def costos(request):
    
    context={
        
    }
    return render(request, 'costos/costos.html',context)