# Generated by Django 3.2 on 2021-05-07 12:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conf_app', '0002_auto_20210507_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='participants',
            field=models.ManyToManyField(related_name='guests', to=settings.AUTH_USER_MODEL),
        ),
    ]
