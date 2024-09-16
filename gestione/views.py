# gestione/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Stazione, Pompa, Componente, Controllo, Riparazione
from .forms import StazioneForm, PompaForm, ComponenteForm, ControlloForm, RiparazioneForm
from django.contrib.auth.decorators import login_required


def home(request):
    stazioni = Stazione.objects.all()
    return render(request, 'home.html', {'stazioni': stazioni})

@login_required
def dettagli_stazione(request, stazione_id):
    stazione = get_object_or_404(Stazione, pk=stazione_id)
    return render(request, 'dettagli_stazione.html', {'stazione': stazione}) 

@login_required
def panoramica_stazioni(request):
    stazioni = Stazione.objects.all().prefetch_related(
        'pompa_set',
        'pompa_set__componente_set',
        'controllo_set',
    )
    return render(request, 'panoramica_stazioni.html', {'stazioni': stazioni})

@login_required
def nuova_stazione(request):
    if request.method == 'POST':
        form = StazioneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StazioneForm()
    return render(request, 'nuova_stazione.html', {'form': form})

@login_required
def modifica_stazione(request, stazione_id):
    stazione = get_object_or_404(Stazione, pk=stazione_id)
    if request.method == 'POST':
        form = StazioneForm(request.POST, instance=stazione)
        if form.is_valid():
            form.save()
            return redirect('dettagli_stazione', stazione_id=stazione.id)
    else:
        form = StazioneForm(instance=stazione)
    return render(request, 'modifica_stazione.html', {'form': form, 'stazione': stazione})

@login_required
def nuova_pompa(request):
    stazione_id = request.GET.get('stazione_id')
    if request.method == 'POST':
        form = PompaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dettagli_stazione', stazione_id=form.cleaned_data['stazione'].id)
    else:
        if stazione_id:
            stazione = get_object_or_404(Stazione, pk=stazione_id)
            form = PompaForm(initial={'stazione': stazione})
        else:
            form = PompaForm()
    return render(request, 'nuova_pompa.html', {'form': form})


@login_required
def modifica_pompa(request, pompa_id):
    pompa = get_object_or_404(Pompa, pk=pompa_id)
    if request.method == 'POST':
        form = PompaForm(request.POST, instance=pompa)
        if form.is_valid():
            form.save()
            return redirect('dettagli_pompa', pompa_id=pompa.id)
    else:
        form = PompaForm(instance=pompa)
    return render(request, 'modifica_pompa.html', {'form': form, 'pompa': pompa})

@login_required
def elimina_stazione(request, stazione_id):
    stazione = get_object_or_404(Stazione, pk=stazione_id)
    if request.method == 'POST':
        stazione.delete()
        return redirect('home')
    return render(request, 'elimina_stazione.html', {'stazione': stazione})


# Create your views here.
