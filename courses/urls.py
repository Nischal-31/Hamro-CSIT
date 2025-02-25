# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('semester-list/', views.semester_list_view, name='semester-list'),
    path('semester-detail/<str:pk>/', views.semester_detail_view, name='semester-detail'),
    path('semester-create/', views.semester_create_view, name='semester-create'),
    path('semester-update/<str:pk>/', views.semester_update_view, name='semester-update'),
    path('semester-delete/<str:pk>/', views.semester_delete_view, name='semester-delete'),
    
    path('subject-list/', views.subject_list_view, name='subject-list'),
    path('subject-detail/<str:pk>/', views.subject_detail_view, name='subject-detail'),
    path('subject-create/', views.subject_create_view, name='subject-create'),
    path('subject-update/<str:pk>/', views.subject_update_view, name='subject-update'),
    path('subject-delete/<str:pk>/', views.subject_delete_view, name='subject-delete'),
]
