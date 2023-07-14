# Generated by Django 4.2.2 on 2023-07-14 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0005_alter_resume_previous_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education_degree',
            field=models.CharField(max_length=200, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_years',
            field=models.IntegerField(verbose_name='Опыт работы'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='previous_employment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Предыдущее место работы'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Профессия'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='salary',
            field=models.IntegerField(blank=True, null=True, verbose_name='Желаемая зарплата'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='specialization',
            field=models.CharField(max_length=255, verbose_name='Специализация'),
        ),
    ]