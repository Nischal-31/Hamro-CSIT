from django.db import models

class Semester(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)  # Only allow 1–8
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['number']  # Ensure semesters are always ordered correctly

    def __str__(self):
        return f"Semester {self.number}"


class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveIntegerField(default=3)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['semester', 'name']  # Order by semester and name

    def __str__(self):
        return f"{self.name} (Sem {self.semester.number})"


class Syllabus(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name="syllabus")
    objectives = models.TextField(blank=True, null=True)
    content = models.TextField()  # Markdown or JSON format can be used
    references = models.JSONField(blank=True, null=True)  # Store references as JSON

    def __str__(self):
        return f"Syllabus of {self.subject.name}"


class Chapter(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()  # Helps in ordering chapters

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.syllabus.subject.name}"
