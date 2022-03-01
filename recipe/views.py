
# Create your views here.

'''def recipe(request):
    return render(request, 'recipe.html', {})'''
from django.shortcuts import render
from recipe.models import Recipe

def recipe_index(request):
    rps = Recipe.objects.all()
    context = {
        'rps': rps
    }
    return render(request, 'recipe_index.html', context)

def recipe_detail(request, pk):
    rp = Recipe.objects.get(pk=pk)
    context = {
        'rp': rp
    }
    return render(request, 'recipe_detail.html', context)