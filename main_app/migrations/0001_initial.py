# Generated by Django 4.1.2 on 2022-10-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('mark', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
            ],
        ),
    ]
