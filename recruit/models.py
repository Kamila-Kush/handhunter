from django.db import models
from django.contrib.auth.models import User

class Recruiter(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete= models.CASCADE,
        related_name="recruiter"
    )
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Город")
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name="Страна")
    payment_for_found = models.IntegerField(null=True, blank=True)
    bonus_percent = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)

    # def __str__(self):
    #     return self.user
    class Meta:
        verbose_name = 'Рекрутер'
        verbose_name_plural = 'Рекрутеры'



