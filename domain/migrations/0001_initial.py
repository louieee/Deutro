# Generated by Django 3.2.4 on 2021-06-11 12:22

from django.db import migrations, models
import domain.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'API'), (1, 'BASE'), (2, 'ADMIN'), (3, 'SUB DOMAIN')], default=1)),
            ],
            managers=[
                ('objects', domain.models.DomainManager()),
            ],
        ),
    ]
