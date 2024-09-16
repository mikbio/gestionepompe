from django.contrib import admin
from .models import Stazione, Pompa, Componente, Controllo, Riparazione

admin.site.register(Stazione)
admin.site.register(Pompa)
admin.site.register(Componente)
admin.site.register(Controllo)
admin.site.register(Riparazione)


# Register your models here.
