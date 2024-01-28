from django.contrib import admin
from principal.views import inicio, login
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
      
    path('usuarios/',include('usuarios.urls')),
    
]

