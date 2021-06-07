from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'^api', 'Deutro.api_urls', name="my_api"),
    host(r'^api.(\w+)', 'Deutro.api_urls', name='api'),
    host(r'(\w+)*', 'Deutro.frontend_urls', name='www'),

)