from django.urls import path
from . import views

urlpatterns = [
    # API Overview
    path('', views.apiOverview, name="api-overview"),
    
    # Semester URLs
    path('semester-list/', views.semesterList, name="semester-list-api"),
    path('semester-detail/<str:pk>/', views.semesterDetail, name="semester-detail-api"),
    path('semester-create/', views.semesterCreate, name="semester-create-api"),
    path('semester-update/<str:pk>/', views.semesterUpdate, name="semester-update-api"),
    path('semester-delete/<str:pk>/', views.semesterDelete, name="semester-delete-api"),

    # Subject URLs
    path('subject-list/', views.subjectList, name="subject-list-api"),
    path('subject-detail/<str:pk>/', views.subjectDetail, name="subject-detail-api"),
    path('subject-create/', views.subjectCreate, name="subject-create-api"),
    path('subject-update/<str:pk>/', views.subjectUpdate, name="subject-update-api"),
    path('subject-delete/<str:pk>/', views.subjectDelete, name="subject-delete-api"),


    # Syllabus URLs
    path('syllabus-list/', views.syllabusList, name="syllabus-list-api"),
    path('syllabus-detail/<str:pk>/', views.syllabusDetail, name="syllabus-detail-api"),
    path('syllabus-create/', views.syllabusCreate, name="syllabus-create-api"),
    path('syllabus-update/<str:pk>/', views.syllabusUpdate, name="syllabus-update-api"),
    path('syllabus-delete/<str:pk>/', views.syllabusDelete, name="syllabus-delete-api"),

    # Chapter URLs
    path('chapter-list/', views.chapterList, name="chapter-list-api"),
    path('chapter-detail/<str:pk>/', views.chapterDetail, name="chapter-detail-api"),
    path('chapter-create/', views.chapterCreate, name="chapter-create-api"),
    path('chapter-update/<str:pk>/', views.chapterUpdate, name="chapter-update-api"),
    path('chapter-delete/<str:pk>/', views.chapterDelete, name="chapter-delete-api"),
]
