# Generated by Django 3.1.14 on 2023-03-02 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20230301_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_eng',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 2, 23, 21, 9, 981227)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 2, 23, 21, 9, 981227)),
        ),
    ]
