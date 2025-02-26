from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status
from .models import Subject,Syllabus,Chapter,Semester,Course,Note,PastQuestion

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import SubjectSerializer,SyllabusSerializer,ChapterSerializer,SemesterSerializer,CourseSerializer,NotesSerializer,PastQuestionsSerializer      
from django.urls import reverse

#-----------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Courses": {
            "List": request.build_absolute_uri(reverse('course-list-api')),
            "Detail View": request.build_absolute_uri(reverse('course-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('course-create-api')),
            "Update": request.build_absolute_uri(reverse('course-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('course-delete-api', args=['<id>']))
        },
        "Subjects": {
            "List": request.build_absolute_uri(reverse('subject-list-api')),
            "Detail View": request.build_absolute_uri(reverse('subject-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('subject-create-api')),
            "Update": request.build_absolute_uri(reverse('subject-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('subject-delete-api', args=['<id>']))
        },
        "Notes": {
            "List": request.build_absolute_uri(reverse('note-list-api')),
            "Detail View": request.build_absolute_uri(reverse('note-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('note-create-api')),
            "Update": request.build_absolute_uri(reverse('note-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('note-delete-api', args=['<id>']))
        },
        "PastQuestions": {
            "List": request.build_absolute_uri(reverse('pastQuestion-list-api')),
            "Detail View": request.build_absolute_uri(reverse('pastQuestion-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('pastQuestion-create-api')),
            "Update": request.build_absolute_uri(reverse('pastQuestion-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('pastQuestion-delete-api', args=['<id>']))
        },
        "Syllabus": {
            "List": request.build_absolute_uri(reverse('syllabus-list-api')),
            "Detail View": request.build_absolute_uri(reverse('syllabus-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('syllabus-create-api')),
            "Update": request.build_absolute_uri(reverse('syllabus-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('syllabus-delete-api', args=['<id>']))
        },
        "Semesters": {
            "List": request.build_absolute_uri(reverse('semester-list-api')),
            "Detail View": request.build_absolute_uri(reverse('semester-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('semester-create-api')),
            "Update": request.build_absolute_uri(reverse('semester-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('semester-delete-api', args=['<id>']))
        },
        "Chapters": {
            "List": request.build_absolute_uri(reverse('chapter-list-api')),
            "Detail View": request.build_absolute_uri(reverse('chapter-detail-api', args=['<id>'])),
            "Create": request.build_absolute_uri(reverse('chapter-create-api')),
            "Update": request.build_absolute_uri(reverse('chapter-update-api', args=['<id>'])),
            "Delete": request.build_absolute_uri(reverse('chapter-delete-api', args=['<id>']))
        }
    }

    return Response(api_urls)

#-------------------------------------------------------------------------------------------------------------------------------

#-------------------------COURSE-----------------------------------

@api_view(['POST'])
def courseCreate(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def courseList(request):
    courses = Course.objects.all().order_by('id')  # Ensuring ordered query
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def courseDetail(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course)
    return Response(serializer.data)

@api_view(['POST'])
def courseUpdate(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    # Updating fields
    name = request.data.get("name")
    description = request.data.get("description")

    if name:
        course.name = name
    if description:
        course.description = description

    try:
        course.save()
    except Exception as e:
        return Response({'error': f"Failed to update course: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CourseSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def courseDelete(request, pk):
    try:
        course = Course.objects.get(id=pk)
        course.delete()
        return Response({'message': 'Course successfully deleted!'}, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
#--------------------------------------------------------------------------------------------------------------------

#-------------------------SEMESTER-----------------------------------

@api_view(['POST'])
def semesterCreate(request):
    serializer = SemesterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def semesterList(request):
    semesters = Semester.objects.all().order_by('id')  # Ensure queryset is ordered
    serializer = SemesterSerializer(semesters, many=True)
    return Response(serializer.data)

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
        # Fetch the semester object
        semester = Semester.objects.get(id=pk)
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)

    # Get updated fields from the request data
    number = request.data.get("number")
    description = request.data.get("description")

    # Update the semester fields
    if number:
        semester.number = number
    if description:
        semester.description = description

    # Save the changes
    try:
        semester.save()
    except Exception as e:
        return Response({'error': f"Failed to update semester: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # Return the updated data
    serializer = SemesterSerializer(semester)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
 

@api_view(['GET'])
def subjectList(request):
    subjects = Subject.objects.all().order_by('id')  # Ensure queryset is ordered
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


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

#-------------------------NOTES-----------------------------------    
@api_view(['POST'])
def noteCreate(request):
    if request.method == 'POST':
        data = request.data.copy()
        
        # Extract file from request.FILES
        file = request.FILES.get('file')

        # Ensure a file was uploaded
        if not file:
            return Response({'error': 'No file uploaded'}, status=400)
        
        # Create and save note
        serializer = NotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save(file=file)
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def noteList(request):
    notes = Note.objects.all().order_by('id')
    serializer = NotesSerializer(notes, many=True,context={'request':request})
    return Response(serializer.data)

@api_view(['GET'])
def noteDetail(request,pk):
    note = Note.objects.get(id=pk)
    serializer= NotesSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def noteUpdate(request,pk):
    note = Note.objects.get(id=pk)
    serializer=NotesSerializer(instance=note ,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
def noteDelete(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note successfully Deleted!')

#--------------------------------------------------------------------------------------------------------------------

#-------------------------OLDQUESTIONS-----------------------------------   

@api_view(['POST'])
def pastQuestionCreate(request):
    data = request.data.copy()
    subject_id = data.get('subject')

    # Check if the subject exists
    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found'}, status=status.HTTP_400_BAD_REQUEST)

    # Assign the subject instance
    data['subject'] = subject.id

    serializer = PastQuestionsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pastQuestionList(request):
    pastquestions = PastQuestion.objects.all().order_by('id')
    serializer = PastQuestionsSerializer(pastquestions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pastQuestionDetail(request,pk):
    pastquestion = PastQuestion.objects.get(id=pk)
    serializer= PastQuestionsSerializer(pastquestion,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def pastQuestionUpdate(request,pk):
    pastquestion = PastQuestion.objects.get(id=pk)
    serializer=PastQuestionsSerializer(instance=pastquestion ,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
def pastQuestionDelete(request,pk):
    pastquestion = PastQuestion.objects.get(id=pk)
    pastquestion.delete()
    return Response('Note successfully Deleted!')

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


@api_view(['GET'])
def syllabusList(request):
    syllabuses = Syllabus.objects.all().order_by('id')
    serializer = SyllabusSerializer(syllabuses, many=True)

    return Response(serializer.data)


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

@api_view(['GET'])
def chapterList(request):
    chapters = Chapter.objects.all().order_by('id')
    serializer = ChapterSerializer(chapters, many=True)

    return Response(serializer.data)


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