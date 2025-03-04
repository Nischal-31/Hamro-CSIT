from rest_framework import serializers
from django.conf import settings
from .models import Subject,Semester,Syllabus,Chapter,Course,Note,PastQuestion

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'image']

    def get_image(self, obj):
        # Ensure that we are using the request context to build the absolute URL
        request = self.context.get('request')  # Get the current request
        if request:
            # Build the absolute URL using the request object
            return request.build_absolute_uri(obj.image.url)  # Build the full URL
        return obj.image.url  # Fallback to the relative URL if request is not found

class SemesterSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all()) 
    class Meta:
        model = Semester
        fields = ['id', 'course', 'number', 'description']
 
class SubjectSerializer(serializers.ModelSerializer):
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    course = serializers.SerializerMethodField()  # Fetch course via semester

    class Meta:
        model = Subject
        fields = ['id', 'semester', 'course', 'name', 'code', 'credits', 'description']

    def get_course(self, obj):
        # Access course through the semester relationship
        return CourseSerializer(obj.semester.course).data

class PastQuestionsSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta:
        model = PastQuestion
        fields = ['id', 'subject', 'year', 'title', 'description', 'file']
             
class SyllabusSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta: 
        model = Syllabus
        fields = ['id', 'subject', 'objectives', 'content', 'references']

class ChapterSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta:
        model = Chapter
        fields = ['id', 'subject', 'title', 'description', 'order']

class NotesSerializer(serializers.ModelSerializer):
    chapter = serializers.PrimaryKeyRelatedField(queryset=Chapter.objects.all())
    class Meta:
        model = Note
        fields = ['id', 'chapter', 'title', 'description', 'file']
        
    def get_file(self, obj):
        # Ensure that we are using the request context to build the absolute URL
        request = self.context.get('request')  # Get the current request
        if request:
            # Build the absolute URL using the request object
            return request.build_absolute_uri(obj.file.url)  # Build the full URL
        return obj.file.url  # Fallback to the relative URL if request is not found
    


