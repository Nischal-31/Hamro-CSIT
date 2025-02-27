from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', views.index, name ='index'),

    path('accounts/', include('allauth.urls')),
    path('courses/', include('courses.urls')),
    
	##### user related path########################## 
	path('user/', include('user.urls')),
    path('syllabus_api/', include('syllabus_api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)