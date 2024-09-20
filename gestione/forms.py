# gestione/forms.py

from django import forms
from .models import Stazione, Pompa, Componente, Controllo, Riparazione

class StazioneForm(forms.ModelForm):
    class Meta:
        model = Stazione
        fields = ['nome', 'comune', 'note']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'comune': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PompaForm(forms.ModelForm):
    stazione = forms.ModelChoiceField(
        queryset=Stazione.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Stazione'
    )

    class Meta:
        model = Pompa
        fields = ['stazione', 'numero_serie', 'modello', 'girante', 'kw', 'prevalenza', 'posizione', 'note']
        widgets = {
            'numero_serie': forms.TextInput(attrs={'class': 'form-control'}),
            'modello': forms.TextInput(attrs={'class': 'form-control'}),
            'girante': forms.TextInput(attrs={'class': 'form-control'}),
            'kw': forms.NumberInput(attrs={'class': 'form-control'}),
            'prevalenza': forms.NumberInput(attrs={'class': 'form-control'}),
            'posizione': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


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
