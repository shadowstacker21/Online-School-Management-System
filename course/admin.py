from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Department,CoursePurchase

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CoursePurchase)
