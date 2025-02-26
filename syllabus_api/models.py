from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

#{
#    "name": "Computer Science",
#    "description": "This course covers the fundamentals of computer science, including programming, algorithms, and data structures."
#}

class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="semesters")
    number = models.IntegerField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Semester {self.number} - {self.course.name}"

#{
#    "course": 1,   (id of course)
#    "number": 1,
#    "description": "First semester covering basic programming and mathematics."
#}

class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)  # Foreign key reference to Semester
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField(default=3)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Sem {self.semester.number})"
    
#{
#    "semester": 1,  (id of semester)
#    "name": "Object-Oriented Programming",
#    "code": "CSIT201",
#    "credits": 3,
#    "description": "This course covers object-oriented programming concepts using C++."
#}

    
class Note(models.Model):
    subject = models.ForeignKey(Subject, related_name="notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='notes/')  # File upload for the notes

    def __str__(self):
        return self.title
    
#{
#    "id": 1,
#    "subject": 1,
#    "title": "OOP Basics",
#    "file": "/media/notes/oop-intro.pdf",
#    "description": "Introduction to Object-Oriented Programming."
#}

class PastQuestion(models.Model):
    subject = models.ForeignKey(Subject, related_name="past_questions", on_delete=models.CASCADE)
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='past_questions/')  # File upload for the past question papers

    def __str__(self):
        return f"Past Question {self.year} - {self.title}"

class Syllabus(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name="syllabus")
    objectives = models.TextField(blank=True, null=True)
    content = models.JSONField()  # Markdown or JSON format can be used
    references = models.JSONField(blank=True, null=True)  # List of reference books/resources

    def __str__(self):
        return f"Syllabus of {self.subject.name}"
    

class Chapter(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()  # Helps in ordering chapters

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} - {self.syllabus.subject.name}"
