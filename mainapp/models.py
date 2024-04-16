from django.db import models
from goodseller.settings import API_DESCRIPTION_CHOICES, URL_DESCRIPTION_CHOICES, REQUEST_TYPES_CHOICES
from django.utils import timezone
import json


class Individ(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    family = models.CharField(max_length=50, blank=False)
    fullname = models.CharField(max_length=150)
    shortfullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    phone = models.CharField(max_length=12, unique=True, blank=False)
    address_registration = models.CharField(max_length=250)
    address_residential = models.CharField(max_length=250)
    registration_date = models.DateField(default=timezone.now, blank=False)
    status = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return f'{self.shortfullname}, e-mail: {self.email}, моб.: {self.phone}'


class Employe(models.Model):
    jobtitle = models.CharField(max_length=50, blank=False)
    individ = models.ForeignKey(Individ, on_delete=models.PROTECT)
    salary = models.PositiveIntegerField(default=0)
    startjob = models.DateField()
    status = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return f'Сотрудник: {self.individ}, должность: {self.jobtitle}, вступил в должность: {self.startjob}'


class Company(models.Model):
    shortname = models.CharField(max_length=50, blank=False)
    longname = models.CharField(max_length=100, blank=False)
    inn = models.CharField(max_length=12, unique=True, blank=False)
    ogrn = models.CharField(max_length=15, unique=True, blank=False)
    address_registration = models.CharField(max_length=250)
    registration_date = models.DateField()
    director = models.ForeignKey(Employe, on_delete=models.PROTECT)
    status = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return f'{self.shortname}, инн: {self.inn}, огрн: {self.ogrn}'

    @staticmethod
    def get_company():
        choices_company = ()
        companys = Company.objects.all()
        for company in companys:
            choices_company.add((company.pk, company.shortname))
        return choices_company


class APIKey(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=False)
    # пока ключ должен быть либо универсальным, либо иметь одно предназначение
    # (например, статистика, аналитика или отзывы и ответы и т.д.)
    description = models.CharField(max_length=50, choices=API_DESCRIPTION_CHOICES, blank=False)
    key = models.CharField(max_length=500, unique=True, blank=False)
    lastusage = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'API key {self.description} для {self.company}'


class APIUrl(models.Model):
    url = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=50, choices=URL_DESCRIPTION_CHOICES, blank=False)
    request = models.CharField(max_length=10, choices=REQUEST_TYPES_CHOICES, default='PUT')
    validity = models.DateField()

    def __str__(self):
        return f'API url {self.description}, действует до {self.validity}'
