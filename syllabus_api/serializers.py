from rest_framework import serializers
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
        
class PastQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastQuestion
        fields = '__all__'

