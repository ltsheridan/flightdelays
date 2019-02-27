# Generated by Django 2.1.3 on 2019-02-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightdelays', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Flight delay',
                'verbose_name_plural': 'Flight delays',
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Flight delay',
                'verbose_name_plural': 'Flight delays',
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Flight delay',
                'verbose_name_plural': 'Flight delays',
                'db_table': 'state',
                'managed': False,
            },
        ),
    ]
