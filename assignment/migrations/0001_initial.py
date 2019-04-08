# Generated by Django 2.1.4 on 2019-01-10 01:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_given', models.DateTimeField()),
                ('submission_date', models.DateTimeField()),
                ('subject', models.IntegerField(choices=[(1, 'Elementary Science'), (2, 'Integrated Science')])),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image', models.ImageField(default=None, upload_to='images/')),
                ('file', models.FileField(default=None, upload_to='assignments/')),
                ('stage', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(6)])),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
        ),
    ]
