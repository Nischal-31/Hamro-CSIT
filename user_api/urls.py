from django.urls import path
from . import views

urlpatterns = [
     # API Overview
    path('', views.apiOverview, name="api-overview"),
    
    # Course URLs
    path('user-list/', views.userList, name="user-list-api"),
    path('user-detail/<str:pk>/', views.userDetail, name="user-detail-api"),
    path('user-create/', views.userCreate, name="user-create-api"),
    path('user-update/<str:pk>/', views.userUpdate, name="user-update-api"),
    path('user-delete/<str:pk>/', views.userDelete, name="user-delete-api"),
]
