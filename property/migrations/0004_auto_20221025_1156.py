# Generated by Django 2.2.24 on 2022-10-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(default=False, null=True, verbose_name='Новостройка'),
        ),
    ]
