from rest_framework import generics, permissions
from user.models import CustomUser
from .serializers import UserSerializer

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer    
from django.urls import reverse


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Users": {
            "List": request.build_absolute_uri(reverse('user-list-api')),
            "Detail View": request.build_absolute_uri(reverse('user-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('user-create-api')),
            "Update": request.build_absolute_uri(reverse('user-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('user-delete-api', args=['<id>']))
        }
    }
    return Response(api_urls)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def userList(request):
    users = CustomUser.objects.all().order_by('id')  # Ensuring ordered query
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    try:
        user = CustomUser.objects.get(id=pk)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
    try:
        user = CustomUser.objects.get(id=pk)  # Attempt to retrieve user by pk
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Proceed to update user fields (excluding user_type)
    username = request.data.get("username")
    email = request.data.get("email")
    phone_no = request.data.get("phone_no")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")

    if username:
        user.username = username
    if email:
        user.email = email
    if phone_no:
        user.phone_no = phone_no
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    try:
        user.save()  # Attempt to save the updated user
    except Exception as e:
        return Response({'error': f"Failed to update user: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Return the updated user data
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def userDelete(request, pk):
    try:
        user = CustomUser.objects.get(id=pk)
        user.delete()
        return Response({'message': 'User successfully deleted!'}, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
