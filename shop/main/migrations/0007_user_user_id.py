# Generated by Django 4.2.2 on 2023-06-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_image_user_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
