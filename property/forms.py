from django import forms
from multiupload.fields import MultiImageField
from .models import *

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address', 'country','city','district','street']


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = ['type']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_type','name']


class MediaPropertyForm(forms.ModelForm):
    class Meta:
        model = MediaProperty
        fields = ['property', 'photo']

    """def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            validate_video(video)
        return video
    """
    

class DescriptionForm(forms.ModelForm):

    images = MultiImageField(min_num=1, max_num=10, max_file_size=1024*1024*5)

    class Meta:
        model = Description
        fields = ['description']
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'property_type']

class AppartementDetailsForm(forms.ModelForm):
    class Meta:
        model = AppartementDetails
        fields = ['count_bedroom', 'count_bathroom','superficie']

class DuplexDetailsForm(forms.ModelForm):
    class Meta:
        model = DuplexDetails
        fields = ['count_bedroom', 'count_bathroom','superficie']

class ImmeubleDetailsForm(forms.ModelForm):
    class Meta:
        model = ImmeubleDetails
        fields = ['count_level', 'count_appartement','count_studio','count_bedroom', 'superficie']
