# Generated by Django 3.2.6 on 2021-09-03 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentcomment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='landmarkcomment',
            name='id',
        ),
        migrations.AlterField(
            model_name='contentcomment',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='contentComments', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='landmarkcomment',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='landmarkComments', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
