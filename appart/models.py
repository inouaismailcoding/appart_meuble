from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os


# Create your models here.

def validate_video(value):
    ext = os.path.splitext(value.name)[1]  # Obtient l'extension du fichier
    valid_extensions = ['.mp4', '.avi', '.mkv', '.mov']  # Liste des extensions vidéo autorisées
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Format de fichier vidéo non pris en charge.'))

class Country(models.Model):
    """
    Modèle représentant un pays.
    """
    name = models.CharField(max_length=100, verbose_name='Nom du pays')

    def __str__(self):
        return self.name


class City(models.Model):
    """
    Modèle représentant une ville.
    """
    name = models.CharField(max_length=100, verbose_name='Nom de la ville')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Pays')

    def __str__(self):
        return f"{self.name}, {self.country}"

class District(models.Model):
    """
    Modèle représentant un arrondissement.
    """
    name = models.CharField(max_length=100, verbose_name='Nom de l\'arrondissement')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ville')

    def __str__(self):
        return f"{self.name}, {self.city}"

class Street(models.Model):
    """
    Modèle représentant une rue.
    """
    name = models.CharField(max_length=100, verbose_name='Nom de la rue')
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Arrondissement')

    def __str__(self):
        return f"{self.name}, {self.district}"
class PropertyType(models.Model):
    """
    Modèle représentant les types de propriété.
    """
    name = models.CharField(max_length=100, verbose_name='Nom du type de propriété')

    def __str__(self):
        return self.name

class Property(models.Model):
    """
    Modèle représentant une propriété immobilière.
    """
    address = models.CharField(max_length=255, verbose_name='Adresse')
    description = models.TextField(blank=True, verbose_name='Description')
    bedrooms = models.PositiveIntegerField(verbose_name='Nombre de chambres')
    bathrooms = models.PositiveIntegerField(verbose_name='Nombre de salles de bains')
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Montant du loyer')
    available_for_rent = models.BooleanField(default=True, verbose_name='Disponible à la location')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Pays')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ville')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Arrondissement')
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Rue')

    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Type de propriété')

    def __str__(self):
        return f"{self.address} - {self.property_type}"


# models.py
from django.db import models

class MediaProperty(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Type de propriété')
    photo1 = models.ImageField(upload_to='appartement_photos/',null=True,blank=True)
    photo2 = models.ImageField(upload_to='appartement_photos/',null=True,blank=True)
    photo3 = models.ImageField(upload_to='appartement_photos/',null=True,blank=True)
    photo4 = models.ImageField(upload_to='appartement_photos/',null=True,blank=True)
    photo5 = models.ImageField(upload_to='appartement_photos/',null=True,blank=True)
    photo6 = models.ImageField(upload_to='appartement_photos/',null=True,blank=True)
    video = models.FileField(upload_to='appartement_videos/', validators=[validate_video], null=True, blank=True)

