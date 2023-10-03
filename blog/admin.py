from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin) :
    list_display = ['title', 'autor', 'created_time']

class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Todo,TodoAdmin)