from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from student.views import HomeView, AboutView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomeView.as_view()),
                  path('home/', HomeView.as_view(), name='home'),
                  path('teacher/', include('teacher.urls')),
                  path('student/', include('student.urls')),
                  path('schools/', include('school.urls')),
                  path('admin/', include('card.urls')),
                  path('account/', include('account.urls')),
                  path('about_us/', AboutView.as_view(), name='about'),
                  url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
