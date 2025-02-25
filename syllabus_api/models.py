from django.db import models

class Semester(models.Model):
    number = models.IntegerField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Semester {self.number}"

class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)  # Foreign key reference to Semester
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField(default=3)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Sem {self.semester.number})"

class Syllabus(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name="syllabus")
    objectives = models.TextField(blank=True, null=True)
    content = models.JSONField()  # Markdown or JSON format can be used
    references = models.JSONField(blank=True, null=True)  # List of reference books/resources

    def __str__(self):
        return f"Syllabus of {self.subject.name}"
    
#{like:
#  "subject": 1,
#  "objectives": "To understand the basic principles of computer science.",
#  "content": "1. Introduction to Programming\n2. Data Structures\n3. Algorithms",
#  "references": ["Introduction to Algorithms - Cormen", "Python Programming - Zed Shaw"]
#}    
    
class Chapter(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()  # Helps in ordering chapters

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} - {self.syllabus.subject.name}"
