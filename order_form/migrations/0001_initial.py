# Generated by Django 3.2.3 on 2021-06-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up', models.CharField(max_length=150)),
                ('deliver', models.CharField(max_length=150)),
                ('weight', models.IntegerField()),
                ('size', models.IntegerField()),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
