from rest_framework import serializers
from .models import Subject,Semester,Syllabus,Chapter

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'
 
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
             
class SyllabusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Syllabus
        fields = '__all__'  

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
