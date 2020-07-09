# Generated by Django 2.2.13 on 2020-07-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('awarding_body', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField()),
            ],
        ),
    ]
