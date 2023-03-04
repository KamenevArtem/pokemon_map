import datetime
from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField(verbose_name='Название покемона')
    image = models.ImageField(
        null=True,
        verbose_name='Изображение покемона'
        )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
        )
    title_eng = models.TextField(
        blank=True,
        verbose_name='Название покемона на английском языке'
        )
    title_jp =  models.TextField(
        blank=True,
        verbose_name='Название покемона на японском языке'
        )
    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='Из кого эволюционировал',
        on_delete=models.CASCADE,
        related_name='next_evolution',
        )
    
    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    last = models.FloatField(verbose_name='Название покемона на английском языке')
    long = models.FloatField(verbose_name='Название покемона на английском языке')
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Название покемона'
        )
    appeared_at = models.DateTimeField(
        default=datetime.datetime.now(),
        verbose_name='Время появления'
        )
    disappeared_at = models.DateTimeField(
        default=datetime.datetime.now(),
        verbose_name='Время исчезновения'
        )
    level = models.IntegerField(
        null=True,
        verbose_name='Уровень'
        )
    health = models.IntegerField(
        null=True,
        verbose_name='Количество здоровья'
        )
    strength = models.IntegerField(
        null=True,
        verbose_name='Сила'
        )
    defence = models.IntegerField(
        null=True,
        verbose_name='Защита'
        )
    stamina = models.IntegerField(
        null=True,
        verbose_name='Выносливость'
        )

