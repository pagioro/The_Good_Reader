# Generated by Django 3.2 on 2023-03-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugreport', '0002_rename_resolution_bugreport_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
