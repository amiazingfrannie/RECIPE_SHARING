from django.contrib import admin

# Register your models here.

from recipe.models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
      search_fields = ('title',)
