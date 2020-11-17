from django.db import models
from datetime import date


class Employee(models.Model):
    name = models.CharField(verbose_name='Name', unique=True, max_length=100)
    salary = models.DecimalField(verbose_name='Salary', decimal_places=2, max_digits=8)
    position = models.CharField(verbose_name='Position name', max_length=100)

    def __str__(self):
        return self.name


class Excursion(models.Model):
    name = models.CharField(verbose_name='Exc name', unique=True, max_length=100)
    date = models.DateField(verbose_name='Exc start', default=date.today)
    term = models.PositiveSmallIntegerField(verbose_name='Term exc', default=1)
    price = models.DecimalField(verbose_name='Exc price', decimal_places=2, max_digits=8)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(verbose_name='Hall name', max_length=100)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exhibit(models.Model):
    name = models.CharField(verbose_name='Exhibit name', max_length=100)
    author = models.CharField(verbose_name='Atuhor name', max_length=100)
    material = models.CharField(verbose_name='Material name', max_length=100)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
