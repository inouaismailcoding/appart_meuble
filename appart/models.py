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


