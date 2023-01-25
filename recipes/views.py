
from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Recipe


# Create your views here.
def home(request):
    # Para importar todas as receitas, ordenadas utilizando o método de order_by
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    recipes = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipes,
        'is_detail_page': True,
    })
