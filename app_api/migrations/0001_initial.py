# Generated by Django 5.0.2 on 2024-02-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('Student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('hosteler', models.BooleanField(default=False)),
            ],
        ),
    ]
