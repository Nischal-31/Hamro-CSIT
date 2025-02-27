from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', views.index_view, name ='index'),
    path('about/', views.about_view, name ='about'),
    path('blog/', views.blog_view, name ='blog'),
    path('course/', views.course_view, name ='course'),
    path('contact/', views.contact_view, name ='contact'),
    path('post/', views.post_view, name ='post'),


    path('accounts/', include('allauth.urls')),
    path('courses/', include('courses.urls')),
    
    
	##### user related path########################## 
	path('user/', include('user.urls')),
    path('syllabus_api/', include('syllabus_api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)