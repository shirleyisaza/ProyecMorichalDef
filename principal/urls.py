from django.contrib import admin
from principal.views import inicio, login
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
<<<<<<< HEAD
    
    path('usuarios/',include('usuarios.urls')),
   
=======
      
    path('usuarios/',include('usuarios.urls')),
    
>>>>>>> e63aa6997ffde7c707585a8be1060c20aeae71e5
]

