from django.shortcuts import render
from course.serializers import CreateCourseSerializer,CreateDepartMentSerializerUserOrTeacher,AdminSerializer,UserSerializer,CreateDepartMentSerializer
from rest_framework.viewsets import ModelViewSet
from course.models import Course,Department,CoursePurchase
from api.permissions import IsAdminOrTeacherOwner,IsAdminOnly
from course.paginatons import DefaultPagination
from course.filters import CourseFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
# Create your views here.

class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminOrTeacherOwner]
    pagination_class = DefaultPagination
    search_field = ['department']
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class =  CourseFilter

    def get_serializer_class(self):
       if self.request.user.role == 'teacher':
           return CreateCourseSerializer
       if self.request.user.role == 'admin':
           return AdminSerializer
       return UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Course.objects.select_related('department').select_related('teacher').all()
        elif user.role == 'teacher':
            return Course.objects.filter(teacher=user)
        return Course.objects.select_related('department').select_related('teacher').all()

    def perform_create(self,serializer):
        if self.request.user.role == 'teacher':
            serializer.save(teacher = self.request.user)

        elif self.request.user.role == 'admin':
            serializer.save()



class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [IsAdminOnly]

    def get_serializer_class(self):
       if self.request.user.role == 'admin':
           return CreateDepartMentSerializer
       return CreateDepartMentSerializerUserOrTeacher
    

    # kalke course purchase and admin dashboard er kaj korte hobe