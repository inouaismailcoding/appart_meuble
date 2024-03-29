# Generated by Django 5.0.1 on 2024-01-28 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appart', '0009_alter_property_property_type'),
        ('property', '0004_country_property_propertytype_city_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='property',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='mediaproperty',
            name='property',
        ),
        migrations.DeleteModel(
            name='PropertyType',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='MediaProperty',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
