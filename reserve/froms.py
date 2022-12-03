from .models import PlayTime
from django.forms import ModelForm

class PlayTimeForm(ModelForm):
    class Meta:
        model = PlayTime
        fields = 'system',
