from django.shortcuts import render, redirect
from . import models
from . import form
from django.contrib import messages
from django.utils.html import format_html

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


# Mantenimiento de Pokemons
def pokelist(request):
    
    pokemons = models.Pokemon.objects.all()
    
    return render(request, "pokemons/lista_pokemon.html", {"pokelist":pokemons})

def add_pokemon(request):
    
    if request.method == "GET":
        form_pokemon = form.PokemonForm(request.GET)
        return render(request, "pokemons/pokeform.html", {"form":form_pokemon})
    
    if request.method == "POST":
        form_pokemon = form.PokemonForm(request.POST, request.FILES)
        if form_pokemon.is_valid():
            form_pokemon.save()
            return redirect("pokelist")
        return render(request, "pokeform.html", {"form":form_pokemon})

def edit_pokemon(request, id):
    pokemon = models.Pokemon.objects.get(id=id)

    if request.method == "GET":
        form_pokemon = form.PokemonForm(instance=pokemon)
        return render(request, "pokemons/pokedit.html", {"form": form_pokemon, "id": id})

    if request.method == "POST":
        form_pokemon = form.PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form_pokemon.is_valid():
            form_pokemon.save()
            messages.success(request, 'La información del Pokémon se ha actualizado')
        return render(request, "pokemons/pokedit.html", {"form": form_pokemon, "id": id})

def pokedelete(request, id):
    
    pokemons = models.Pokemon.objects.get(id=id)
    if request.method == "GET":
        pokemons.delete()
        messages.success(request, format_html('<strong>El pokemon a sido eliminado</strong>'))
        return redirect("pokelist")
    # return render(request, "lista_pokemon.html", {""})
# ! REGION
def regionlist(request):
    region = models.Region.objects.all()
    return render(request, "regiones/lista_region.html", {"region":region})

def add_region(request):
    
    if request.method == "GET":
        form_region = form.RegionForm(request.GET)
        return render(request, "regiones//regionform.html", {"form":form_region})
    
    if request.method == "POST":
        form_region = form.RegionForm(request.POST)
        if form_region.is_valid():
            form_region.save()
        return redirect("regiones")

def edit_region(request, id):
    region = models.Region.objects.get(id=id)
    
    if request.method == "GET":
        form_region = form.RegionForm(instance=region)
        return render(request, "regiones/edit_region.html", {"form":form_region, "id":id})
    
    if request.method == "POST":
        form_region = form.RegionForm(request.POST, instance=region)
        if form_region.is_valid():
            form_region.save()
            messages.success(request, 'Se a actualizado la region.')
            return redirect("regiones")
    
def delete_region(request, id):
    region = models.Region.objects.get(id=id)
    if request.method == "GET":
        region.delete()
        messages.success(request, 'Se a Eliminado la region')
        return redirect("regiones")
    
# ! TIPOS
def kinds(request):
    
    kinds_query = models.Kind.objects.all()
    
    return render(request, "tipos/lista_tipos.html", {"kinds":kinds_query})

def add_kind(request):
    
    if request.method == "GET":
        form_kind = form.KindForm()
        return render(request, "tipos/tiposform.html", {"form":form_kind})
    
    if request.method == "POST":
        form_kind = form.KindForm(request.POST)
        if form_kind.is_valid():
            form_kind.save()
            messages.success(request, "El tipo a sido creado")
        return render(request, "tipos/tiposform.html", {"form":form_kind})
    
def edit_kind(request, id):
    kind = models.Kind.objects.get(id=id)
    if request.method == "GET":
        form_kind = form.KindForm(instance=kind)
        return render(request, "tipos/edit_tipos.html", {"form":form_kind, "id":id})
    
    if request.method == "POST":
        form_kind = form.KindForm(request.POST, instance=kind)
        if form_kind.is_valid():
            form_kind.save()
            messages.success(request, f"Se a actulizado el tipo {kind.name_kind}.")
            return redirect("kinds")

def delete_kind(request, id):
    kind = models.Kind.objects.get(id=id)
    if request.method == "GET":
        kind.delete()
        messages.success(request, "El tipo se a borrado con exito.")
        return redirect("kinds")
        

