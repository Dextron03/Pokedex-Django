from django.shortcuts import render, redirect
from . import models
from . import form

def index(request):
    # Obtiene todas los regiones para mostrar en el formulario
    regions = models.Region.objects.all()

    # Obtiene toods los pokémon filtrados por nombre
    pokemons = models.Pokemon.objects.all()

    if 'search' in request.GET:
        search_query = request.GET.get('search', "")
        pokemons = pokemons.filter(name__contains=search_query)

    # Obtiene todos los pokémon filtrados por regiones seleccionadas
    if 'regions' in request.GET:
        selected_regions = request.GET.getlist('regions')
        pokemons = pokemons.filter(id_region__in=selected_regions)

    return render(request, "index.html", {"pokemon": pokemons, "regions": regions})


def add_pokemon(request):
    
    if request.method == "GET":
        form_pokemon = form.PokemonForm(request.GET)
        return render(request, "pokeform.html", {"form":form_pokemon})
    
    if request.method == "POST":
        form_pokemon = form.PokemonForm(request.POST, request.FILES)
        if form_pokemon.is_valid():
            form_pokemon.save()
            return redirect("home")
        return render(request, "pokeform.html", {"form":form_pokemon})
            
    
    