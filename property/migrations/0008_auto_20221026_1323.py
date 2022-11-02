# Generated by Django 2.2.24 on 2022-10-26 10:23

from django.db import migrations
from django.db.models import F


def define_new_building(apps, schema_editor):
    flats_model = apps.get_model('property', 'Flat')

    flats_model.objects.all().update(new_building=F('construction_year' > 2010))


def move_backward_new_building(apps, schema_editor):
    flats_model = apps.get_model('property', 'Flat')

    flats_model.objects.all().update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20221026_1321'),
    ]

    operations = [
        migrations.RunPython(define_new_building, move_backward_new_building)
    ]
