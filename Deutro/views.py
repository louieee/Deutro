# Create your views here.
from django.views.generic import View
from .models import *
from django.utils import timezone
from .PDF import Render


class Pdf(View):

    def get(self, request):
        sales = Sales.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request}
        return Render.render('pdf.html', params)
