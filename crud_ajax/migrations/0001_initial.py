# Generated by Django 2.0.2 on 2020-12-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('roll_no', models.CharField(blank=True, max_length=100)),
                ('class_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]