# Generated by Django 2.2.6 on 2019-11-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agrement_details', models.CharField(max_length=2048, verbose_name='Agrement')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opperator_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('Shop_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('address', models.FileField(upload_to='pictures/', verbose_name='Profile Picture')),
                ('location', models.CharField(max_length=250, verbose_name='First Name')),
                ('city', models.CharField(max_length=250, verbose_name='First Name')),
            ],
            options={
                'db_table': 'shops',
            },
        ),
    ]
