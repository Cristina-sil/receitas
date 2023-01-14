from django.urls import path

from . import views

app_name = 'recipes'
# recipes:recipe, ou recipes:home

urlpatterns = [
    path('', views.home, name='home'),  # HOME
    path('recipes/<int:id>/', views.recipes,
         name='recipe'),  # detail page

]
