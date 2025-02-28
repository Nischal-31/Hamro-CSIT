from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', views.index_view, name ='index'),
    path('about/', views.about_view, name ='about'),
    path('course/', views.course_view, name ='course'),
    path('course-inner/', lambda request: render(request, 'course-inner.html'), name='course-inner'),

    path('accounts/', include('allauth.urls')),
    path('courses/', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('contactenquiry/', include('contactenquiry.urls')),
    
    
	##### user related path########################## 
	path('user/', include('user.urls')),
    path('syllabus_api/', include('syllabus_api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)