from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField('Новостройка', default=None, null=True)

    likes = models.ManyToManyField(User, verbose_name='Кто лайкнул', blank=True, related_name='liked_flats')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто жалуется', related_name='complaints')
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, verbose_name='Квартира на которую жалуются', related_name='complaints')
    complaint = models.TextField('Текст жалобы')

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'

    def __str__(self):
        return f'Пользователь: {self.user.name}, ID квартиры: {self.flat.pk}'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=250, db_index=True)
    phonenumber = models.CharField('Номер владельца', max_length=20)
    pure_phone = PhoneNumberField('Нормализированный номер владельца', blank=True, max_length=20)
    flats = models.ManyToManyField('Flat', verbose_name='Квартиры в собственности', related_name='owners', db_index=True)

    class Meta:
        verbose_name = 'Собственник'
        verbose_name_plural = 'Собственники'

    def __str__(self):
        return self.name

