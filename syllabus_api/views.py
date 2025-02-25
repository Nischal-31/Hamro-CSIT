from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status
from .models import Subject,Syllabus,Chapter,Semester

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import SubjectSerializer,SyllabusSerializer,ChapterSerializer,SemesterSerializer
from django.urls import reverse

#-----------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Subjects": {
            "List": request.build_absolute_uri(reverse('subject-list')),
            "Detail View": request.build_absolute_uri(reverse('subject-detail', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('subject-create')),
            "Update": request.build_absolute_uri(reverse('subject-update', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('subject-delete', args=['<id>']))
        },
        "Syllabus": {
            "List": request.build_absolute_uri(reverse('syllabus-list')),
            "Detail View": request.build_absolute_uri(reverse('syllabus-detail', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('syllabus-create')),
            "Update": request.build_absolute_uri(reverse('syllabus-update', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('syllabus-delete', args=['<id>']))
        },
        "Semesters": {
            "List": request.build_absolute_uri(reverse('semester-list')),
            "Detail View": request.build_absolute_uri(reverse('semester-detail', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('semester-create')),
            "Update": request.build_absolute_uri(reverse('semester-update', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('semester-delete', args=['<id>']))
        },
        "Chapters": {
            "List": request.build_absolute_uri(reverse('chapter-list')),
            "Detail View": request.build_absolute_uri(reverse('chapter-detail', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('chapter-create')),
            "Update": request.build_absolute_uri(reverse('chapter-update', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('chapter-delete', args=['<id>']))
        }
    }

    return Response(api_urls)

#--------------------------------------------------------------------------------------------------------------------

#-------------------------SEMESTER-----------------------------------

class SemesterPagination(PageNumberPagination):
    page_size = 10  # Customize the number of semesters per page
    page_size_query_param = 'page_size'  # Allow overriding with query param
    max_page_size = 100  # Limit the max page size


@api_view(['POST'])
def semesterCreate(request):
    serializer = SemesterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def semesterList(request):
    semesters = Semester.objects.all()
    
    # Paginate the results
    paginator = SemesterPagination()
    result_page = paginator.paginate_queryset(semesters, request)
    serializer = SemesterSerializer(result_page, many=True)
    
    # Return paginated data with a URL for the next page
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def semesterDetail(request, pk):
    try:
        semester = Semester.objects.get(id=pk)
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SemesterSerializer(semester, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def semesterUpdate(request, pk):
    try:
        semester = Semester.objects.get(id=pk)
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SemesterSerializer(instance=semester, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def semesterDelete(request, pk):
    try:
        semester = Semester.objects.get(id=pk)
        semester.delete()
        return Response('Semester successfully deleted!')
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
#--------------------------------------------------------------------------------------------------------------------

#-------------------------SUBJECT-----------------------------------    
    

@api_view(['POST'])
def subjectCreate(request):
    # Get a mutable copy of the request data
    data = request.data.copy()

    # Get the semester_id from the request
    semester_id = data.get('semester')

    # Check if the semester_id exists
    try:
        semester = Semester.objects.get(id=semester_id)
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_400_BAD_REQUEST)

    # Assign the correct semester instance to data
    data['semester'] = semester.id

    # Serialize and save
    serializer = SubjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
class SubjectPagination(PageNumberPagination):
    page_size = 10  # Customize the number of subjects per page
    page_size_query_param = 'page_size'  # Allow overriding with query param
    max_page_size = 100  # Limit the max page size

@api_view(['GET'])
def subjectList(request):
    subjects = Subject.objects.all()
    
    # Paginate the results
    paginator = SubjectPagination()
    result_page = paginator.paginate_queryset(subjects, request)
    serializer = SubjectSerializer(result_page, many=True)
    
    # Return paginated data with a URL for the next page
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def subjectDetail(request,pk):
    subjects = Subject.objects.get(id=pk)
    serializer= SubjectSerializer(subjects,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def subjectUpdate(request,pk):
    subject = Subject.objects.get(id=pk)
    serializer=SubjectSerializer(instance=subject ,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
def subjectDelete(request,pk):
    subject = Subject.objects.get(id=pk)
    subject.delete()
    return Response('Subject successfully Deleted!')

#--------------------------------------------------------------------------------------------------------------------

#-------------------------SYLLABUS-----------------------------------    

@api_view(['POST'])
def syllabusCreate(request):
    subject_id = request.data.get('subject')

    # Check if a syllabus for this subject already exists
    syllabus, created = Syllabus.objects.get_or_create(subject_id=subject_id)

    serializer = SyllabusSerializer(syllabus, data=request.data, partial=True)  # Allow partial updates

    if serializer.is_valid():
        serializer.save()
        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)  # Updated syllabus

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SyllabusPagination(PageNumberPagination):
    page_size = 10  # Customize the number of syllabuses per page
    page_size_query_param = 'page_size'  # Allow overriding with query param
    max_page_size = 100  # Limit the max page size

@api_view(['GET'])
def syllabusList(request):
    syllabuses = Syllabus.objects.all()
    
    # Paginate the results
    paginator = SyllabusPagination()
    result_page = paginator.paginate_queryset(syllabuses, request)
    serializer = SyllabusSerializer(result_page, many=True)
    
    # Return paginated data with a URL for the next page
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def syllabusDetail(request, pk):
    try:
        syllabus = Syllabus.objects.get(id=pk)
    except Syllabus.DoesNotExist:
        return Response({'error': 'Syllabus not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SyllabusSerializer(syllabus, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def syllabusUpdate(request, pk):
    try:
        syllabus = Syllabus.objects.get(id=pk)
    except Syllabus.DoesNotExist:
        return Response({'error': 'Syllabus not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SyllabusSerializer(instance=syllabus, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def syllabusDelete(request, pk):
    try:
        syllabus = Syllabus.objects.get(id=pk)
        syllabus.delete()
        return Response('Syllabus successfully deleted!')
    except Syllabus.DoesNotExist:
        return Response({'error': 'Syllabus not found'}, status=status.HTTP_404_NOT_FOUND)

#--------------------------------------------------------------------------------------------------------------------

#-------------------------CHAPTER-----------------------------------    

@api_view(['POST'])
def chapterCreate(request):
    serializer = ChapterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChapterPagination(PageNumberPagination):
    page_size = 10  # Customize the number of chapters per page
    page_size_query_param = 'page_size'  # Allow overriding with query param
    max_page_size = 100  # Limit the max page size

@api_view(['GET'])
def chapterList(request):
    chapters = Chapter.objects.all()
    
    # Paginate the results
    paginator = ChapterPagination()
    result_page = paginator.paginate_queryset(chapters, request)
    serializer = ChapterSerializer(result_page, many=True)
    
    # Return paginated data with a URL for the next page
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def chapterDetail(request, pk):
    try:
        chapter = Chapter.objects.get(id=pk)
    except Chapter.DoesNotExist:
        return Response({'error': 'Chapter not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ChapterSerializer(chapter, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def chapterUpdate(request, pk):
    try:
        chapter = Chapter.objects.get(id=pk)
    except Chapter.DoesNotExist:
        return Response({'error': 'Chapter not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ChapterSerializer(instance=chapter, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def chapterDelete(request, pk):
    try:
        chapter = Chapter.objects.get(id=pk)
        chapter.delete()
        return Response('Chapter successfully deleted!')
    except Chapter.DoesNotExist:
        return Response({'error': 'Chapter not found'}, status=status.HTTP_404_NOT_FOUND)

#-----------------------------------------------------------------------------------------------------------------------------