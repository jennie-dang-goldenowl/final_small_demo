# Generated by Django 4.0.3 on 2022-04-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateField(),
        ),
    ]
