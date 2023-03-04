import datetime
from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(null=True)
    description = models.TextField(blank=True)
    title_eng = models.TextField(blank=True)
    title_jp =  models.TextField(blank=True)
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
    last = models.FloatField()
    long = models.FloatField()
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE
        )
    appeared_at = models.DateTimeField(
        default=datetime.datetime.now()
        )
    disappeared_at = models.DateTimeField(
        default=datetime.datetime.now()
        )
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)

