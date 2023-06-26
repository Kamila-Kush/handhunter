from django.db import models
from django.contrib.auth.models import User
class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True, blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
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


class CV(models.Model):
    name = models.CharField(max_length=200)
    education_degree = models.CharField(max_length=200)
    age = models.IntegerField()
    experience_years = models.IntegerField()
    previous_employment = models.CharField(max_length=255)

    worker = models.ForeignKey(
        to=Worker,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return self.name