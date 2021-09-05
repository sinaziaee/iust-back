from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('<str:course>/home/', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('schedule/', views.schedule, name='schedule'),  # {host}/{course}/api/home/
    path('lecture/', views.lecture, name='lecture'),  # {host}/{course}/api/schedule/
    path('assignment/', views.assignment, name='assignment'),  # {host}/{course}/api/lecture/
    path('final_project/', views.final_project, name='final_project'),  # {host}/{course}/api/final_project/
    path('course_material/', views.course_material, name='course_material'),  # {host}/{course}/api/course_material/
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
