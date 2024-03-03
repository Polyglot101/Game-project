from django.urls import path
from .views import main, game, results, rules  # Changed 'result' to 'results'

urlpatterns = [
    path('', main, name='main'),
    path('game/', game, name='game'),
    path('result/', results, name='results'),  # Changed 'result' to 'results'
    path('rules/', rules, name='rules'),
]
