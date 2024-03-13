from django.forms import ModelForm
from deportista.models import Deportista

class DeportistaForm(ModelForm):
    class Meta:
        model= Deportista
        fields= "__all__"
        exclude=["estado",]
        