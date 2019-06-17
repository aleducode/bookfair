"""Fair models"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    """Image Model"""
    footer = models.CharField(
        'Pie de foto',
        max_length=255,
        null=True, blank=True
    )
    photo = models.ImageField(
        'Foto',
        upload_to='section/notices')

    def __str__(self):
        """returrn title"""
        return self.footer


class Post(models.Model):
    """Post model """

    title = models.CharField('Título', max_length=500)
    photo = models.ManyToManyField(Image)
    lead = models.CharField('Lead Noticia', max_length=500)
    text = models.TextField('Texto Noticia')

    #metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """returrn title"""
        return self.title

class Guest(models.Model):
    """Guest Model"""
    name = models.CharField('Nombre', max_length=500)
    title = models.CharField('Titulo', max_length=500)
    message = models.CharField('Mensaje', max_length=500)
    photo = models.ImageField(
        'Foto',
        upload_to='section/guests')
        
    def __str__(self):
        """returrn title"""
        return self.title

