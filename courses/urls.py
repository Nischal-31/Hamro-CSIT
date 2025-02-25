# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('subject-list/', views.subject_list_view, name='subject-list'),
    path('subject-detail/<int:pk>/', views.subject_detail_view, name='subject-detail'),
    path('subject-create/', views.subject_create_view, name='subject-create'),
    path('subject-update/<int:pk>/', views.subject_update_view, name='subject-update'),
    path('subject-delete/<int:pk>/', views.subject_delete_view, name='subject-delete'),
]
