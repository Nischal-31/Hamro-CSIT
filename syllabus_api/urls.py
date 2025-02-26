from django.urls import path
from . import views

urlpatterns = [
    # API Overview
    path('', views.apiOverview, name="api-overview"),
    
    # Course URLs
    path('course-list/', views.courseList, name="course-list-api"),
    path('course-detail/<str:pk>/', views.courseDetail, name="course-detail-api"),
    path('course-create/', views.courseCreate, name="course-create-api"),
    path('course-update/<str:pk>/', views.courseUpdate, name="course-update-api"),
    path('course-delete/<str:pk>/', views.courseDelete, name="course-delete-api"),
    
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
    
    # Notes URLs
    path('note-list/', views.noteList, name="note-list-api"),
    path('note-detail/<str:pk>/', views.noteDetail, name="note-detail-api"),
    path('note-create/', views.noteCreate, name="note-create-api"),
    path('note-update/<str:pk>/', views.noteUpdate, name="note-update-api"),
    path('note-delete/<str:pk>/', views.noteDelete, name="note-delete-api"),
    
     # PastQuestions URLs
    path('pastQuestion-list/', views.pastQuestionList, name="pastQuestion-list-api"),
    path('pastQuestion-detail/<str:pk>/', views.pastQuestionDetail, name="pastQuestion-detail-api"),
    path('pastQuestion-create/', views.pastQuestionCreate, name="pastQuestion-create-api"),
    path('pastQuestion-update/<str:pk>/', views.pastQuestionUpdate, name="pastQuestion-update-api"),
    path('pastQuestion-delete/<str:pk>/', views.pastQuestionDelete, name="pastQuestion-delete-api"),
    

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
