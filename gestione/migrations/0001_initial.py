# Generated by Django 4.2.1 on 2024-09-16 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pompa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(max_length=100)),
                ('modello', models.CharField(max_length=100)),
                ('data_installazione', models.DateField()),
                ('stato', models.CharField(choices=[('sede', 'In Sede'), ('deposito', 'In Deposito'), ('officina', 'In Officina')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ubicazione', models.CharField(max_length=200)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Riparazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_riparazione', models.DateField()),
                ('descrizione', models.TextField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pompa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.pompa')),
            ],
        ),
        migrations.AddField(
            model_name='pompa',
            name='stazione',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.stazione'),
        ),
        migrations.CreateModel(
            name='Controllo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_controllo', models.DateField()),
                ('note', models.TextField(blank=True, null=True)),
                ('stazione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.stazione')),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('risalita', 'Risalita'), ('valvola', 'Valvola di Non Ritorno'), ('galleggiante_max', 'Galleggiante Massimo'), ('galleggiante_min', 'Galleggiante Minimo'), ('saracinesca', 'Saracinesca')], max_length=20)),
                ('stato', models.CharField(max_length=100)),
                ('data_sostituzione', models.DateField(blank=True, null=True)),
                ('pompa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestione.pompa')),
            ],
        ),
    ]
