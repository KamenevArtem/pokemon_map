import folium

from django.utils.timezone import localtime
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_on_page = []
    for pokemon in pokemons:
        image_url = request.build_absolute_uri(pokemon.image.url)
        pokemons_on_page.append({
            'pokemon_id': pokemon.pk,
            'img_url': image_url,
            'title_ru': pokemon.title,
        })
    time_now = localtime()
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').filter(
        disappeared_at__gte=time_now,
        appeared_at__lte=time_now
    )
    for entity in pokemon_entities:
        add_pokemon(
            folium_map, entity.lat,
            entity.long,
            image_url
        )
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon_entities = PokemonEntity.objects.filter(pokemon=requested_pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    previous_evo_pokemon_description = {}
    next_evo_pokemon_description = {}
    if requested_pokemon.previous_evolution:
        previous_evo_pokemon = requested_pokemon.previous_evolution
        previous_evo_pokemon_description = {
            'pokemon_id': previous_evo_pokemon.pk,
            'img_url': previous_evo_pokemon.image.url,
            'title_ru': previous_evo_pokemon.title,
        }
    if requested_pokemon.pokemons.first():
        next_evo_pokemon = requested_pokemon.pokemons.first()
        next_evo_pokemon_description = {
                'pokemon_id': next_evo_pokemon.pk,
                'img_url': next_evo_pokemon.image.url,
                'title_ru': next_evo_pokemon.title,
            }
    pokemon_description = {
        'title_ru': requested_pokemon.title,
        'img_url': requested_pokemon.image.url,
        'title_en': requested_pokemon.title_eng,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.description,
        'pokemon_id': requested_pokemon.pk,
        'previous_evolution': previous_evo_pokemon_description,
        'next_evolution': next_evo_pokemon_description
    }
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.long,
            request.build_absolute_uri(requested_pokemon.image.url)
        )
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_description
    })
