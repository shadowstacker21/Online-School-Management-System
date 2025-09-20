from rest_framework import serializers
from course.models import Course,CoursePurchase,Department

class CreateCourseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    dept_name = serializers.SerializerMethodField(method_name='get_department_name')
    teacher_name = serializers.SerializerMethodField(method_name='get_teacher_name')
    class Meta:
        model = Course
        fields = ['id','title','description','image','department','dept_name','teacher','teacher_name','price']
        read_only_fields = ['teacher']

    def get_department_name(self,obj):
        return obj.department.name if obj.department else None
    def get_teacher_name(self,obj):
        return obj.teacher.get_full_name() if obj.teacher else None

class AdminSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    dept_name = serializers.SerializerMethodField(method_name='get_department_name')
    teacher_name = serializers.SerializerMethodField(method_name='get_teacher_name')
    class Meta:
        model = Course
        fields = ['id','title','description','image','department','dept_name','teacher','teacher_name','price']

    def get_department_name(self,obj):
        return obj.department.name if obj.department else None
    def get_teacher_name(self,obj):
        return obj.teacher.get_full_name() if obj.teacher else None
    
class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    dept_name = serializers.SerializerMethodField(method_name='get_department_name')
    teacher_name = serializers.SerializerMethodField(method_name='get_teacher_name')
    class Meta:
        model = Course
        fields = ['id','title','description','image','department','dept_name','teacher','teacher_name','price']
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


class CoursePurchaseSerializer(serializers.ModelSerializer):
    student_email = serializers.EmailField(source='student.email', read_only=True)
    student_name = serializers.EmailField(source='student.first_name', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_price = serializers.DecimalField(source='course.price', read_only=True)
    class Meta:
        model = CoursePurchase
        fields = ['id','student_email','student_name','course','course_title','course_price','status','purchased_at']
        read_only_fields = ['id','student_email','student_name','course','course_title','course_price','status','purchased_at']

    def create(self,validated_data):
        student = self.context['request'].user
        
        validated_data['student'] = student
        return super().create(validated_data)
       
    

        