# Generated by Django 4.2.2 on 2023-06-08 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_user_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brands',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Order_Details',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='sneakers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.sneakers'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
