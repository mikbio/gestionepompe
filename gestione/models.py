from django.db import models

class Stazione(models.Model):
    nome = models.CharField(max_length=100)
    ubicazione = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Pompa(models.Model):
    numero_serie = models.CharField(max_length=100)
    modello = models.CharField(max_length=100)
    data_installazione = models.DateField()
    STATO_CHOICES = [
        ('sede', 'In Sede'),
        ('deposito', 'In Deposito'),
        ('officina', 'In Officina'),
    ]
    stato = models.CharField(max_length=10, choices=STATO_CHOICES)
    stazione = models.ForeignKey(Stazione, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modello} ({self.numero_serie})"

class Componente(models.Model):
    TIPO_CHOICES = [
        ('risalita', 'Risalita'),
        ('valvola', 'Valvola di Non Ritorno'),
        ('galleggiante_max', 'Galleggiante Massimo'),
        ('galleggiante_min', 'Galleggiante Minimo'),
        ('saracinesca', 'Saracinesca'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    stato = models.CharField(max_length=100)
    data_sostituzione = models.DateField(blank=True, null=True)
    pompa = models.ForeignKey(Pompa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} per {self.pompa}"

class Controllo(models.Model):
    data_controllo = models.DateField()
    stazione = models.ForeignKey(Stazione, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Controllo {self.data_controllo} - {self.stazione}"

class Riparazione(models.Model):
    data_riparazione = models.DateField()
    descrizione = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    pompa = models.ForeignKey(Pompa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Riparazione {self.data_riparazione} - {self.pompa}"

# Create your models here.
