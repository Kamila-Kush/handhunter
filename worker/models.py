from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    is_searching = models.BooleanField()

    def __str__(self):
        return self.name