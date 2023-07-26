from django.db import models
from django.contrib.auth.models import User
class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True, blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, verbose_name='Имя')
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    salary = models.IntegerField(null=True, blank=True, verbose_name='Желаемая зарплата')
    is_searching = models.BooleanField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    to_worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    author=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
            )

    def __str__(self):
        return self.author.username


class Resume(models.Model):
    title = models.CharField(max_length=200, verbose_name='Профессия')
    education_degree = models.CharField(max_length=200, verbose_name='Образование')
    age = models.IntegerField(verbose_name='Возраст')
    experience_years = models.IntegerField(verbose_name='Опыт работы')
    previous_employment = models.CharField(max_length=255, null=True, blank=True, verbose_name='Предыдущее место работы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    profile_photo = models.ImageField(
        null=True, blank=True, upload_to="profile_photo/", verbose_name='Фото сотрудника'
    )

    worker = models.ForeignKey(
        to=Worker,
        on_delete = models.CASCADE,
        related_name = 'resume'
    )
    def __str__(self):
        return self.title