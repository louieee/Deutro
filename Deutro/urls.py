from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from student.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home, name='home'),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('schools/', include('school.urls')),
    path('admin/', include('card.urls')),
                  path('account/', include('account.urls')),
                  path('about_us/', about, name='about')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
