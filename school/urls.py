from django.urls import path

from school.views import add_school, school_detail, view_schools

urlpatterns = [
    path('add_school/', add_school, name='add_school'),
    path('', view_schools, name='all_schools'),
    path('<int:school_id>/', school_detail, name='school_detail')
]
