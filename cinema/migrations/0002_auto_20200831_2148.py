# Generated by Django 3.1 on 2020-08-31 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemaperson',
            name='bio',
            field=models.TextField(),
        ),
    ]