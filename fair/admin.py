"""Fair Admin"""

# Django 
from django.contrib import admin

# Models
from fair.models import *

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Guest)
admin.site.register(Program)
admin.site.register(Topic)