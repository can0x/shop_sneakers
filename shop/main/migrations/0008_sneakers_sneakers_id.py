# Generated by Django 4.2.2 on 2023-06-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='sneakers_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
