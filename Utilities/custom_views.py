from django.shortcuts import render
from django.views.generic import View


class DefaultView(View):
    template = None
    context = {}

    def get(self, request):
        self.context['host'] = request.get_host()
        return render(request, self.template, context=self.context)
