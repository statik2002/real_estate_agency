# Generated by Django 2.2.24 on 2022-10-29 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0028_delete_propertyownerownedflats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_complains', to='property.Flat', verbose_name='Квартира на которую жалуются'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comlaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жалуется'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
