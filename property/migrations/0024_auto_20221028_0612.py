# Generated by Django 2.2.24 on 2022-10-28 03:12

from django.db import migrations


def migrate_owner_flats(apps, schema_editor):
    flat_model = apps.get_model('property', 'Flat')
    owner_model = apps.get_model('property', 'Owner')

    owners = owner_model.objects.all()

    for owner in owners.iterator():
        owner_flats = flat_model.objects.filter(owner=owner.name)
        owner.flats.set(owner_flats)
        owner.save()


def migrate_owner_flats_back(apps, schema_editor):
    owner_model = apps.get_model('property', 'Owner')

    owners = owner_model.objects.all()

    for owner in owners.iterator():
        owner.flats.clear()
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0023_auto_20221028_0558'),
    ]

    operations = [
        migrations.RunPython(migrate_owner_flats, migrate_owner_flats_back),
    ]
