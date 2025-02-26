# Generated by Django 2.2.24 on 2022-10-27 03:41
import phonenumbers
from django.db import migrations


def normalize_phone_numbers(apps, schema_editor):
    flat_model = apps.get_model('property', 'Flat')

    flats = flat_model.objects.all()

    for flat in flats.iterator():
        try:
            parsed_phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')

            if not phonenumbers.is_possible_number(parsed_phone_number) or \
                    not phonenumbers.is_valid_number(parsed_phone_number):
                continue

            flat.owner_pure_phone = phonenumbers.format_number(
                parsed_phone_number,
                phonenumbers.PhoneNumberFormat.E164
            )
            flat.save()

        except phonenumbers.phonenumberutil.NumberParseException:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20221027_0625'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
