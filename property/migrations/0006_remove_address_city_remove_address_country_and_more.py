# Generated by Django 5.0.1 on 2024-01-28 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_delete_propertytype_alter_property_property_type'),
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
            model_name='appartementdetails',
            name='property',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='duplexdetails',
            name='property',
        ),
        migrations.RemoveField(
            model_name='immeubledetails',
            name='property',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='AppartementDetails',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='DuplexDetails',
        ),
        migrations.DeleteModel(
            name='ImmeubleDetails',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]