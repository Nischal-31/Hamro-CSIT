from django.contrib import admin
from syllabus_api.models import Course  # Import Course from syllabus_api

#class CourseAdmin(admin.ModelAdmin):
#    list_display = ('name', 'image_preview')
#    search_fields = ('name',)
#    
#    def image_preview(self, obj):
#        if obj.image:
#            return f'<img src="{obj.image.url}" width="50" height="50" style="border-radius:5px;"/>'
#        return "No Image"
#    
#    image_preview.allow_tags = True
#    image_preview.short_description = "Preview"#
#
#admin.site.register(Course, CourseAdmin)
