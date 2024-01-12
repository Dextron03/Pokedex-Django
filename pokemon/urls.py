from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_pokemon/', views.add_pokemon, name="add_pokemon"),
]
