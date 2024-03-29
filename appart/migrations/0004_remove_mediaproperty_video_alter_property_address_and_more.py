# Generated by Django 5.0.1 on 2024-01-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appart', '0003_rename_appartement_mediaproperty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediaproperty',
            name='video',
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nombre de salles de bains'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nombre de chambres'),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='property',
            name='rent_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Montant du loyer'),
        ),
    ]
