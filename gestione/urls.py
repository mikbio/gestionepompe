# gestione/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stazione/<int:stazione_id>/', views.dettagli_stazione, name='dettagli_stazione'),
    path('nuova_stazione/', views.nuova_stazione, name='nuova_stazione'),
    path('stazione/<int:stazione_id>/modifica/', views.modifica_stazione, name='modifica_stazione'),
    path('stazione/<int:stazione_id>/elimina/', views.elimina_stazione, name='elimina_stazione'),
    path('nuova_pompa/', views.nuova_pompa, name='nuova_pompa'),
    path('pompa/<int:pompa_id>/modifica/', views.modifica_pompa, name='modifica_pompa'),
    path('panoramica/', views.panoramica_stazioni, name='panoramica_stazioni'),
    path('pompa/<int:pompa_id>/', views.dettagli_pompa, name='dettagli_pompa'),
]
    # Aggiungi percorsi simili per Componente, Controllo e Riparazione

