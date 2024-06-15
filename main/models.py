from django.db import models
import uuid
from django import forms
from django.core.validators import MinLengthValidator

class Builders(models.Model):
    name = models.CharField("Имя", max_length= 20, blank = False)
    secondname = models.CharField("Фамилия", max_length=20,blank = False)
    patronymic = models.CharField("Отчество", max_length=20, blank = False)
    number = models.CharField("Номер телефона", max_length=10,blank = False)
    status = models.CharField("Cтатус работника",max_length= 100 ,blank = False)

    def __str__(self):
        return f'{self.secondname} {self.name} {self.patronymic}'

class Foremans(models.Model):
    name = models.CharField("Имя", max_length=20, blank=False)
    secondname = models.CharField("Фамилия", max_length=20, blank=False)
    patronymic = models.CharField("Отчество", max_length=20, blank=False)
    number = models.CharField("Номер телефона", max_length=10, blank=False)
    password = models.CharField("Пароль", max_length=15, validators=[MinLengthValidator(4)])
    status = models.CharField("Cтатус работника",max_length= 100 , blank=False)
    def __str__(self):
        return f'{self.secondname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = "Worker"


class Equipment(models.Model):
    name = models.CharField("Имя", max_length=20, blank=False)
    expirydate = models.DateField()
    owner = models.CharField("Владелец", max_length=100, blank = False)
    registersdate = models.DateField("Дата регистрации", auto_now=True, blank = False)
    equipmentphoto = models.ImageField("Фото", blank = False)
    store = models.CharField("Место нахождения",max_length= 100 , blank = False)
    def __str__(self):
        return self.name
class passport_object(models.Model):
    name_object = models.CharField("Имя объекта",max_length= 100 , blank = False)
    orderer = models.CharField("Заказчик",max_length= 100 , blank = False)
    location = models.FloatField("Локация в координатах", blank = False)
class plane(models.Model):
    Task = models.CharField("Задачи", max_length= 100, blank = False)



