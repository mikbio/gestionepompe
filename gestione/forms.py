# gestione/forms.py

from django import forms
from .models import Stazione, Pompa, Componente, Controllo, Riparazione

class StazioneForm(forms.ModelForm):
    class Meta:
        model = Stazione
        fields = ['nome', 'ubicazione', 'note']

class PompaForm(forms.ModelForm):
    class Meta:
        model = Pompa
        fields = ['numero_serie', 'modello', 'data_installazione', 'stato', 'stazione']

    def clean_data_installazione(self):
        data_installazione = self.cleaned_data.get('data_installazione')
        if data_installazione > timezone.now().date():
            raise forms.ValidationError("La data di installazione non può essere nel futuro.")
        return data_installazione


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['tipo', 'stato', 'data_sostituzione', 'pompa']

class ControlloForm(forms.ModelForm):
    class Meta:
        model = Controllo
        fields = ['data_controllo', 'stazione', 'note']

class RiparazioneForm(forms.ModelForm):
    class Meta:
        model = Riparazione
        fields = ['data_riparazione', 'descrizione', 'costo', 'pompa']
