# Generated by Django 3.2.3 on 2021-06-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.RemoveField(
            model_name='header',
            name='email',
        ),
        migrations.RemoveField(
            model_name='header',
            name='phone_one',
        ),
        migrations.RemoveField(
            model_name='header',
            name='phone_two',
        ),
        migrations.AddField(
            model_name='header',
            name='services',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='header',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
