# Generated by Django 2.2.6 on 2019-11-17 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20191114_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agrement',
            name='agrement_details',
            field=models.TextField(max_length=4096, verbose_name='Agrement'),
        ),
    ]
