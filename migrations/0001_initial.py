# Generated by Django 4.2.6 on 2023-10-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=2)),
                ('location', models.CharField(max_length=300)),
            ],
        ),
    ]
