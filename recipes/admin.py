from django.contrib import admin

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe) # registrando
class RecipeAdmin(admin.ModelAdmin):
    ...

# registrando 
admin.site.register(Category, CategoryAdmin)

