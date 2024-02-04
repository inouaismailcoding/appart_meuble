from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    name = models.CharField(max_length=100, verbose_name='Nom du pays')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom de la ville')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Pays')

    def __str__(self):
        return f"{self.name}, {self.country}"

class PropertyType(models.Model):
    APARTMENT = 1
    DUPLEX = 2
    BUILDING = 3
    HOTEL = 4
    STUDIO = 5

    PROPERTY_CHOICES = [
        (APARTMENT, 'Appartement'),
        (DUPLEX, 'Duplex'),
        (BUILDING, 'Immeuble'),
        (HOTEL, 'Hotel'),
        (STUDIO, 'Studio'),
    ]

    type = models.IntegerField(choices=PROPERTY_CHOICES, verbose_name='Nom du type de propriété')
    def __str__(self):
        return dict(self.PROPERTY_CHOICES)[self.type]

class Property(models.Model):
    """
    Modèle représentant une propriété immobilière.
    """
    name= models.CharField(max_length=255, verbose_name='Nom de la propriéte',blank=True,null=True)
    property_type = models.OneToOneField(PropertyType,null=True, blank=True, verbose_name='Type de propriété',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.address} - {self.property_type}"
    
class Address(models.Model):
    property= models.OneToOneField(Property, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Type de propriété')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Pays')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ville')
    district = models.CharField(max_length=200, verbose_name='Nom de l\'arrondissement')
    street = models.CharField(max_length=100, verbose_name='Nom de la rue')
    address = models.CharField(max_length=255, verbose_name='Addresse')

    def __str__(self):
        return f"{self.street} - {self.address} - {self.district}, {self.city}"

class MediaProperty(models.Model):
    property= models.OneToOneField(Property, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Type de propriété')
    photo = models.ImageField(upload_to='property_photo/',null=True,blank=True)
    
    def __str__(self) :
        return f"{self.property.property_type} - {self.property.name}"


#Créer des modèles pour chaque type de propriété avec des détails spécifiques :
class Description(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name='Description',null=True)
    def __str__(self) :
        return f"{self.property.property_type} - {self.property.name}"

class AppartementDetails(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    count_bedroom = models.IntegerField(blank=True,null=True)
    count_bathroom = models.IntegerField(blank=True,null=True)
    #count_saloon = models.IntegerField(blank=True,null=True)
    superficie = models.IntegerField(blank=True,null=True)

class DuplexDetails(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    count_bedroom = models.IntegerField(blank=True,null=True)
    count_bathroom = models.IntegerField(blank=True,null=True)
    #count_saloon = models.IntegerField(blank=True,null=True)
    superficie = models.IntegerField(blank=True,null=True)

class ImmeubleDetails(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    count_level = models.IntegerField(blank=True,null=True)
    count_appartement = models.IntegerField(blank=True,null=True)
    count_studio = models.IntegerField(blank=True,null=True)
    count_bedroom = models.IntegerField(blank=True,null=True)
    superficie = models.IntegerField(blank=True,null=True)



