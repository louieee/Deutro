# Generated by Django 2.1.4 on 2019-01-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0002_result_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='_1st_term_card',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='_2nd_term_card',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='_3rd_term_card',
            field=models.CharField(default=None, max_length=255),
        ),
    ]