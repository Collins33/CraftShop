# Generated by Django 2.0.1 on 2018-01-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craft', '0008_auto_20180125_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craft',
            name='craft_slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
