# Generated by Django 2.2.24 on 2022-10-27 03:25
import phonenumbers
from django.db import migrations


def normalize_phone_numbers(apps, schema_editor):
    flat_model = apps.get_model('property', 'Flat')

    for flat in flat_model.objects.all():
        parsed_phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.owner_pure_phone = phonenumbers.format_number(parsed_phone_number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20221027_0606'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
