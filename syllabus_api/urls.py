from django.urls import path
from . import views

urlpatterns = [
    # API Overview
    path('', views.apiOverview, name="api-overview"),

    # Subject URLs
    path('subject-list/', views.subjectList, name="subject-list"),
    path('subject-detail/<str:pk>/', views.subjectDetail, name="subject-detail"),
    path('subject-create/', views.subjectCreate, name="subject-create"),
    path('subject-update/<str:pk>/', views.subjectUpdate, name="subject-update"),
    path('subject-delete/<str:pk>/', views.subjectDelete, name="subject-delete"),

    # Semester URLs
    path('semester-list/', views.semesterList, name="semester-list"),
    path('semester-detail/<str:pk>/', views.semesterDetail, name="semester-detail"),
    path('semester-create/', views.semesterCreate, name="semester-create"),
    path('semester-update/<str:pk>/', views.semesterUpdate, name="semester-update"),
    path('semester-delete/<str:pk>/', views.semesterDelete, name="semester-delete"),

    # Syllabus URLs
    path('syllabus-list/', views.syllabusList, name="syllabus-list"),
    path('syllabus-detail/<str:pk>/', views.syllabusDetail, name="syllabus-detail"),
    path('syllabus-create/', views.syllabusCreate, name="syllabus-create"),
    path('syllabus-update/<str:pk>/', views.syllabusUpdate, name="syllabus-update"),
    path('syllabus-delete/<str:pk>/', views.syllabusDelete, name="syllabus-delete"),

    # Chapter URLs
    path('chapter-list/', views.chapterList, name="chapter-list"),
    path('chapter-detail/<str:pk>/', views.chapterDetail, name="chapter-detail"),
    path('chapter-create/', views.chapterCreate, name="chapter-create"),
    path('chapter-update/<str:pk>/', views.chapterUpdate, name="chapter-update"),
    path('chapter-delete/<str:pk>/', views.chapterDelete, name="chapter-delete"),
]
