from django.contrib import admin

# Register your models here.
from registrar.models import Student, Class, StudentProject

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(StudentProject)
