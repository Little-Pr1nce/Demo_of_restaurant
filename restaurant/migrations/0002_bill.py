# Generated by Django 2.0.7 on 2018-07-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=10)),
                ('dish_number', models.IntegerField(default=0)),
                ('dish_require', models.CharField(default='无', max_length=50)),
            ],
        ),
    ]
