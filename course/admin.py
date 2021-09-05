from django.contrib import admin
from . import models

admin.site.register(models.Teacher)
admin.site.register(models.TeacherAssistant)
admin.site.register(models.Book)
admin.site.register(models.Announcement)
admin.site.register(models.Schedule)
admin.site.register(models.Lecture)
admin.site.register(models.CourseMaterial)
admin.site.register(models.Assignment)
admin.site.register(models.Policy)
