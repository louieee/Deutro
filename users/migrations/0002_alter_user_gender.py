# Generated by Django 3.2.4 on 2021-06-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'male'), (1, 'female')]),
        ),
    ]
