# Generated by Django 2.2.13 on 2020-08-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='date_completed',
            field=models.CharField(max_length=50),
        ),
    ]