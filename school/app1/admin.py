from django.contrib import admin
from .models import Log,Student,Teacher
# Register your models here.
# admin.site.log_sign_in(Log)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Log)
# admin.site.add_teacher(Teacher)