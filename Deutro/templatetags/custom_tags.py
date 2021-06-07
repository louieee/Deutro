from django import template
from django.http.request import split_domain_port
from django.urls import reverse

from django.http.request import split_domain_port

# print('OUR HOST: ', )

register = template.Library()


@register.simple_tag(name='the_url')
def the_url(request, name, *args, **kwargs):
    return ''.join(('http://', request.get_host(), reverse(name, args=args, kwargs=kwargs)))
