# Generated by Django 2.2.24 on 2022-10-26 09:53

from django.db import migrations


def define_new_building(apps, schema_editor):
    flats_model = apps.get_model('property', 'Flat')

    flats = flats_model.objects.all()

    for flat in flats:
        if flat.construction_year > 2010:
            flat.new_building = True
        else:
            flat.new_building = False

        flat.save()


def move_backward_new_building(apps, schema_editor):
    flats_model = apps.get_model('property', 'Flat')

    flats = flats_model.objects.all()

    for flat in flats:
        flat.new_building = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20221025_1201'),
    ]

    operations = [
        migrations.RunPython(define_new_building, move_backward_new_building)
    ]



