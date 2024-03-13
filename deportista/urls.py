from django.urls import path
from deportista.models import Deportista

urlpatterns = [
    path('Deportista/',Deportista ),
]