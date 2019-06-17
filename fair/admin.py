"""Fair Admin"""

# Django 
from django.contrib import admin

# Models
from fair.models import Post, Image, Guest

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Guest)