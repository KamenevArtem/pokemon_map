# Generated by Django 3.1.14 on 2023-03-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20230305_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время исчезновения'),
        ),
    ]
