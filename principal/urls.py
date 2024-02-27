from django.contrib import admin
from django.urls import path, include
from principal.views import inicio, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('login/', login, name="login"),
    path('costos/',include('costos.urls')),
         
         
]
