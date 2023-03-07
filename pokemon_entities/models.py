from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название покемона'
        )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Изображение покемона'
        )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
        )
    title_eng = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Название покемона на английском языке'
        )
    title_jp = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Название покемона на японском языке'
        )
    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='Из кого эволюционировал',
        on_delete=models.SET_NULL,
        related_name='pokemons',
        )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    long = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Название покемона',
        related_name='pokemons_on_map'
        )
    appeared_at = models.DateTimeField(
        verbose_name='Время появления',
        null=True,
        blank=True,
        )
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения',
        null=True,
        blank=True,
        )
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Уровень'
        )
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Количество здоровья'
        )
    strength = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Сила'
        )
    defence = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Защита'
        )
    stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Выносливость'
        )

    def __str__(self):
        return self.pokemon
