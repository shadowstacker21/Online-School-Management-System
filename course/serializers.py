from rest_framework import serializers
from course.models import Course,CoursePurchase,Department

class CreateCourseSerializer(serializers.ModelSerializer):
    dept_name = serializers.SerializerMethodField(method_name='get_department_name')
    teacher_name = serializers.SerializerMethodField(method_name='get_teacher_name')
    class Meta:
        model = Course
        fields = ['title','description','department','dept_name','teacher','teacher_name','price']
        read_only_fields = ['teacher']

    def get_department_name(self,obj):
        return obj.department.name if obj.department else None
    def get_teacher_name(self,obj):
        return obj.teacher.get_full_name() if obj.teacher else None

class AdminSerializer(serializers.ModelSerializer):
    dept_name = serializers.SerializerMethodField(method_name='get_department_name')
    teacher_name = serializers.SerializerMethodField(method_name='get_teacher_name')
    class Meta:
        model = Course
        fields = ['title','description','department','dept_name','teacher','teacher_name','price']

    def get_department_name(self,obj):
        return obj.department.name if obj.department else None
    def get_teacher_name(self,obj):
        return obj.teacher.get_full_name() if obj.teacher else None
    
class UserSerializer(serializers.ModelSerializer):
    dept_name = serializers.SerializerMethodField(method_name='get_department_name')
    teacher_name = serializers.SerializerMethodField(method_name='get_teacher_name')
    class Meta:
        model = Course
        fields = ['title','description','department','dept_name','teacher','teacher_name','price']
        read_only_fields = fields

    def get_department_name(self,obj):
        return obj.department.name if obj.department else None
    def get_teacher_name(self,obj):
        return obj.teacher.get_full_name() if obj.teacher else None


class CreateDepartMentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name']

class CreateDepartMentSerializerUserOrTeacher(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name']
        read_only_fields = fields
       
    

        