# Generated by Django 4.2.9 on 2024-06-14 16:50

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Builders',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('secondname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('number', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('password', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Пароль')),
                ('status', models.CharField(max_length=100, verbose_name='Cтатус работника')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('expirydate', models.DateField()),
                ('owner', models.CharField(max_length=100, verbose_name='Владелец')),
                ('registersdate', models.DateField(auto_now=True, verbose_name='Дата регистрации')),
                ('equipmentphoto', models.ImageField(upload_to='', verbose_name='Фото')),
                ('store', models.CharField(max_length=100, verbose_name='Место нахождения')),
                ('status', models.CharField(max_length=100, verbose_name='Cтатус транспорта')),
            ],
        ),
        migrations.CreateModel(
            name='Foremans',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('secondname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('password', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Пароль')),
                ('status', models.CharField(max_length=100, verbose_name='Cтатус работника')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Worker',
            },
        ),
        migrations.CreateModel(
            name='passport_object',
            fields=[
                ('name_object', models.CharField(max_length=100, verbose_name='Имя объекта')),
                ('orderer', models.CharField(max_length=100, verbose_name='Заказчик')),
                ('location', models.FloatField(verbose_name='Локация в координатах')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]