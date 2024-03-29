# Generated by Django 5.0.1 on 2024-02-01 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_remove_city_country_alter_immeubledetails_property_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du pays')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom de la propriéte')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('rent_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Montant du loyer')),
                ('available_for_rent', models.BooleanField(default=True, verbose_name='Disponible à la location')),
                ('property_type', models.IntegerField(blank=True, choices=[(1, 'Appartement'), (2, 'Duplex'), (3, 'Immeuble')], null=True, verbose_name='Type de propriété')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom du type de propriété')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom de la ville')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.country', verbose_name='Pays')),
            ],
        ),
        migrations.CreateModel(
            name='MediaProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='appartement_photos/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='appartement_photos/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='appartement_photos/')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='appartement_photos/')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='appartement_photos/')),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.property', verbose_name='Type de propriété')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=200, verbose_name="Nom de l'arrondissement")),
                ('address', models.CharField(max_length=255, verbose_name='Addresse')),
                ('street', models.CharField(max_length=100, verbose_name='Nom de la rue')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.city', verbose_name='Ville')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.country', verbose_name='Pays')),
                ('property', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.property', verbose_name='Type de propriété')),
            ],
        ),
        migrations.AlterField(
            model_name='appartementdetails',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='property.property'),
        ),
        migrations.AlterField(
            model_name='duplexdetails',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='property.property'),
        ),
        migrations.AlterField(
            model_name='immeubledetails',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='property.property'),
        ),
    ]
