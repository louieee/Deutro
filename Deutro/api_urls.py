from django.urls import path, include
urlpatterns = [
                  path('teacher/', include('teacher.apis')),
                  path('student/', include('student.apis')),
                  path('schools/', include('school.apis')),
                  path('admin/', include('card.apis')),
                  path('account/', include('account.apis')),
              ]