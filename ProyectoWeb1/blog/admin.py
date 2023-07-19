from django.contrib import admin
from .models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
