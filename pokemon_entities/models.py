from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    last = models.FloatField()
    long = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
