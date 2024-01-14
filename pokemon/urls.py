from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pokelist/', views.pokelist, name='pokelist'),
    path('add_pokemon/', views.add_pokemon, name="add_pokemon"),
    path('pokedelete/<int:id>/', views.pokedelete, name='pokedelete'),
    path('pokedit/<int:id>/', views.edit_pokemon, name='pokedit'),
    # Regiones
    path('regiones/', views.regionlist, name="regiones"),
    path('add_region/', views.add_region, name="add_region"),
    path('delete_region/<int:id>/',views.delete_region, name="delete_region"),
    path('edit_region/<int:id>/', views.edit_region, name='edit_region'),
    #Tipos
    path("kinds/", views.kinds, name="kinds"),
    path("add_kinds/", views.add_kind, name="add_kind"),
    path("edit_kinds/<int:id>/", views.edit_kind, name="edit_kind"),
    path("delete_kind/<int:id>/", views.delete_kind, name="delete_kind")
    
]
