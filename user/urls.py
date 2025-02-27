from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.Login, name ='login'),
    path('logout/', views.logout_view, name='logout'),
	path('register/', views.register, name ='register'),

]
