# Generated by Django 4.2.2 on 2023-06-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='brand',
            field=models.CharField(default=1, max_length=50, verbose_name='brand'),
            preserve_default=False,
        ),
    ]