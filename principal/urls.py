from django.contrib import admin
from django.urls import path
from principal.views import inicio, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('login/', login, name="login")
]
