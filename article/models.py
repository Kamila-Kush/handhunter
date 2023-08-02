from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticleNew(models.Model):
    author = models.OneToOneField(
        to=User,
        on_delete= models.CASCADE,
        related_name="article_new"
    )
    title = models.CharField(max_length=300, verbose_name='Название статьи')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Время изменений')
    views_count = models.IntegerField(default=0)
    likes_users = models.ManyToManyField(
        to=User,
        blank=True
    )
    def __str__(self):
        return self.title