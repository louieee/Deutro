from decouple import config
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = config('APP_NAME')
admin.site.site_title = f"Admin Portal || || {config('APP_NAME')} || A Complete Django Management System Template"
admin.site.index_title = f"Welcome to {config('APP_NAME')} Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
]
