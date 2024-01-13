from django import forms
from . import models

class PokemonForm(forms.ModelForm):
    class Meta:
        model = models.Pokemon
        fields = '__all__'
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "img": forms.FileInput(attrs={"type": "file", "class": "form-control"}),
            "id_region": forms.Select(attrs={"class": "form-control"}),
            "id_kind": forms.SelectMultiple(attrs={"class": "form-control"})
        }
        
        labels = {
            "name": "Nombre",
            "img": "Imagen",
            "id_region": "Region",
            "id_kind": "Tipo" 
        }



class KindForm(forms.ModelForm):
    class Meta:
        model = models.Kind
        fields = '__all__'
        
        labels = {
            "name_kind":"Tipo"
        }
        
        widgets = {
            "name_kind":forms.TextInput(attrs={"class":"form-control"}),
        }

class RegionForm(forms.ModelForm):
    class Meta:
        model = models.Region
        fields = '__all__'
        
        labels = {
            "name_region": "Region",
        }
        
        error_messages = {
            "name_region":{"required":""}
        }
        
        widgets = {
            "name_region":forms.TextInput(attrs={"class":"form-control"}),
        }
        
        
