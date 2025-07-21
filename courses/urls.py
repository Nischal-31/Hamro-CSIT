# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('course-list/', views.course_list_view, name='course-list'),
    path('course-detail/<str:course_id>/', views.course_detail_view, name='course-detail'),
    path('course-create/', views.course_create_view, name='course-create'),
    path('course-update/<str:course_id>/', views.course_update_view, name='course-update'),
    path('course-delete/<str:course_id>/', views.course_delete_view, name='course-delete'),
    
    path('semester-list/<int:course_id>', views.semester_list_view, name='semester-list'),
    path('semester-detail/<str:semester_id>/', views.semester_detail_view, name='semester-detail'),
    path('semester-create/<int:course_id>', views.semester_create_view, name='semester-create'),
    path('semester-update/<str:semester_id>/', views.semester_update_view, name='semester-update'),
    path('semester-delete/<str:semester_id>/', views.semester_delete_view, name='semester-delete'),
    
    path('subject-list/<int:semester_id>', views.subject_list_view, name='subject-list'),
    path('subject-detail/<str:subject_id>/', views.subject_detail_view, name='subject-detail'),
    path('subject-create/<int:semester_id>', views.subject_create_view, name='subject-create'),
    path('subject-update/<str:subject_id>/', views.subject_update_view, name='subject-update'),
    path('subject-delete/<str:subject_id>/', views.subject_delete_view, name='subject-delete'),

    path('note-list/<int:subject_id>/', views.note_list_view, name='note-list'),

    path('pastQuestion-list/<int:subject_id>/', views.pastQuestion_list_view, name='pastQuestion-list'),
]
