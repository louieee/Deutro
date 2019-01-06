from django.urls import path

from card.views import create_card

urlpatterns = [
    path('create_card/', create_card, name='create_card')
]
