# Generated by Django 3.1.2 on 2021-09-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.BooleanField(default=False)),
            ],
        ),
    ]
