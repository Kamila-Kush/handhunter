from django.db import models
from worker.models import Worker
from django.contrib.auth.models import User

class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вакансия')
    salary = models.IntegerField(null=True, blank=True, verbose_name='Зарплата')
    description = models.TextField(default='Нет описания', verbose_name='Описание')
    is_relevant = models.BooleanField(default=True, verbose_name='Актуально')
    email = models.EmailField(verbose_name='Электронная почта')
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(
        to=Worker,
        blank=True
    )
    view_user = models.ManyToManyField(
        to=User,
        blank=True
    )
    category = models.ForeignKey(
        to='Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['salary']
        unique_together = [['title', 'email']] #

class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

class Company(models.Model):
    title = models.CharField(max_length=255)
    address = models.TextField()
    number_of_employees = models.IntegerField()
    is_hunting = models.BooleanField(default=True)

    def __str__(self):
        return self.title