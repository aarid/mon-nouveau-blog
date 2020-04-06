from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='base'),
    path('jouer/', views.jouer, name='play_button'),
    path('rejoue/', views.replay, name='replay'),
    path('contacter/', views.contacter, name='contacter'),
    path('faq/', views.faq, name='faq'),
    path('qui-sommes-nous/', views.qui_sommes_nous, name='qui_sommes_nous'),
    path('not_found/', views.not_found, name='not_found'),
    path('thanks/', views.thanks, name='thanks'),
    
]
