from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('provience/', views.provience, name='provience'),
    path('provience/<int:provienceId>', cache_page(5)(views.result), name='result')
]
