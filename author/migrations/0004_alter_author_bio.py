# Generated by Django 3.2 on 2022-12-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20221228_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.CharField(max_length=2056),
        ),
    ]
