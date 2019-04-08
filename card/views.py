from django.shortcuts import render
import random , string, json
from card.models import Card


# Create your views here.

def create_card(request):
    if request.method == 'POST':
        chars_base = string.digits + string.ascii_uppercase + string.ascii_lowercase
        pin_code = Card()
        pin_code.code = json.dumps(''.join(random.choice(chars_base) for _ in range(20)))
        pin_code.save()
    return render(request, 'card/create_card.html')
