# Generated by Django 2.0.7 on 2018-07-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('prince', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('number_of_ordering', models.IntegerField(default=0)),
            ],
        ),
    ]
