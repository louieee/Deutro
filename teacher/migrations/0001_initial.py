# Generated by Django 2.1.4 on 2019-01-10 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('subject', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('First_Name', models.CharField(max_length=255)),
                ('Image', models.ImageField(default=None, upload_to='images/')),
                ('Last_Name', models.CharField(max_length=255)),
                ('Gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('stage', models.IntegerField()),
                ('School', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('subject', models.ManyToManyField(to='subject.Subject', verbose_name='subject')),
            ],
        ),
    ]
