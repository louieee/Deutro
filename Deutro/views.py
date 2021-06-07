# Create your views here.
from django.views.generic import View
from django.utils import timezone
from Utilities.python_utils import Render


class Pdf(View):

    def get(self, request):
        sales = {}
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request}
        return Render.render('pdf.html', params)
