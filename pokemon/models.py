from django.db import models
from django.core import validators

# Create your models here.
class Region(models.Model):
    name_region = models.CharField(max_length=75, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name_region
    
    
class Kind(models.Model):
    name_kind = models.CharField(max_length=75, blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name_kind


class Pokemon(models.Model):
    name = models.CharField(max_length=75, blank=False, null=False)
    img = models.ImageField(
        upload_to='pokemon/',
        validators=[validators.FileExtensionValidator(['png', 'jpg', 'jpeg'], message='Formato no permitido, solo admite archivos png, jpg, jpeg')]
    )
    id_region = models.ForeignKey(Region, on_delete= models.CASCADE)
    id_kind = models.ManyToManyField(Kind)
    
    def __str__(self) -> str:
        return self.name