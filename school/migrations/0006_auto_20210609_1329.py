# Generated by Django 3.2.4 on 2021-06-09 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0005_auto_20210609_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='class_s',
            new_name='class_level',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='school',
        ),
        migrations.RemoveField(
            model_name='result',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='class_s',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.AddField(
            model_name='class',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.school'),
        ),
        migrations.AlterField(
            model_name='class',
            name='institution',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Pre School'), (1, 'High School'), (2, 'University')], default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.PositiveSmallIntegerField(choices=[(0, 'First'), (1, 'Second'), (2, 'Third'), (3, 'Fourth'), (4, 'Fifth')], default=None, null=True)),
                ('entry_year', models.DateField()),
                ('report', models.JSONField()),
                ('class_level', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.class')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.session'),
        ),
    ]
