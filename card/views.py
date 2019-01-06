from django.shortcuts import render


# Create your views here.

def create_card(request):
    return render(request, 'card/create_card.html')
