# Generated by Django 3.2.2 on 2021-06-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20190114_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='used',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]