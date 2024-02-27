from django.urls import path

from costos.views import costos


urlpatterns = [
path('', costos,name="costos"),    
]
