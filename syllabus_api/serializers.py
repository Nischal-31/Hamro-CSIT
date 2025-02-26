from rest_framework import serializers
from django.conf import settings
from .models import Subject,Semester,Syllabus,Chapter,Course,Note,PastQuestion

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'
 
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'semester', 'name', 'code', 'credits', 'description']

             
class SyllabusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Syllabus
        fields = '__all__'  

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
    def get_file(self, obj):
        # Ensure that we are using the request context to build the absolute URL
        request = self.context.get('request')  # Get the current request
        if request:
            # Build the absolute URL using the request object
            return request.build_absolute_uri(obj.file.url)  # Build the full URL
        return obj.file.url  # Fallback to the relative URL if request is not found
    
class PastQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastQuestion
        fields = '__all__'

