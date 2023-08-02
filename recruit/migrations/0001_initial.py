# Generated by Django 4.2.2 on 2023-08-02 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна')),
                ('payment_for_found', models.IntegerField(blank=True, null=True)),
                ('bonus_percent', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recruiter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рекрутер',
                'verbose_name_plural': 'Рекрутеры',
            },
        ),
    ]
