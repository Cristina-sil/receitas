from django.urls import path

from . import \
    views  # como o arquivo está na mesma pasta, foi utilizado o ponto, ao invés de from recipes.view import home

urlpatterns = [
    path('', views.home),  # HOME
    path('recipes/<int:id>/', views.recipes),

]
