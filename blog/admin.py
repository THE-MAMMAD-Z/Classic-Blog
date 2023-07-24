from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin) :
    list_display = ['title', 'autor', 'created_time']



admin.site.register(Post,PostAdmin)