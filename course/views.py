from django.shortcuts import render,redirect
from rest_framework.response import Response
from course.serializers import CreateCourseSerializer,CoursePurchaseSerializer,CreateDepartMentSerializerUserOrTeacher,AdminSerializer,UserSerializer,CreateDepartMentSerializer
from rest_framework.viewsets import ModelViewSet
from course.models import Course,Department,CoursePurchase
from api.permissions import IsAdminOrTeacherOwner,IsAdminOnly,IsAdminOrStudentPurchase
from course.paginatons import DefaultPagination
from course.filters import CourseFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view,action
from sslcommerz_lib import SSLCOMMERZ 
from rest_framework import status
import uuid
from django.conf import settings as main_settings
# Create your views here.




class CourseViewSet(ModelViewSet):
    """
   API endpoint for managing course in the project
     - Allow authenticated  admin  to create, update, and delete all course
     - Allow only teacher update their own course
     - Allows users to browse and filter course by department name
     - Student can view all course and purchase
     - Only admin can delete purchase course
   """
    permission_classes = [IsAdminOrTeacherOwner]
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['department__name','title']
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
    """
   API endpoint for managing departmentin the project
     - Allow authenticated  admin to create, update, and delete department
     - Allows authenticated admin only view deprtament
     
     
   """
    queryset = Department.objects.all()
    permission_classes = [IsAdminOnly]

    def get_serializer_class(self):
       if self.request.user.role == 'admin':
           return CreateDepartMentSerializer
       return CreateDepartMentSerializerUserOrTeacher
    

class CoursePurchaseView(ModelViewSet):
    """
   API endpoint for managing purchase course in the online school project
     - Allow authenticated  admin to view all purchases course
     - only student can purchase course and view their own course
    
   """
    serializer_class = CoursePurchaseSerializer
    permission_classes = [IsAdminOrStudentPurchase]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return CoursePurchase.objects.select_related('student','course').all()
        elif user.role == 'student':
            return CoursePurchase.objects.select_related('student','course').filter(student=user)
        return CoursePurchase.objects.none()

    
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)




@api_view(['GET'])
def my_purchases(request):
    user = request.user
    if not user.is_authenticated or getattr(user, 'role', None) != 'student':
        return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    
    purchases = CoursePurchase.objects.select_related('student', 'course').filter(student=user)
    serializer = CoursePurchaseSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def payment_initiate(request):
    user = request.user
    amount = request.data.get("amount")
    tran_id = f"txn_{uuid.uuid4().hex[:12]}"
     
    settings = { 'store_id': 'onlin68cd85b49854a', 
                'store_pass': 'onlin68cd85b49854a@ssl', 
                'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = tran_id
    post_body['success_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/success/"
    post_body['fail_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/fail/"
    post_body['cancel_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/cancel/"
    post_body['emi_option'] = 0
    post_body['cus_name'] = f"{user.first_name} {user.last_name}"
    post_body['cus_email'] = user.email
    post_body['cus_phone'] = user.phone_number
    post_body['cus_add1'] = user.address
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Course"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) 
   
    if response.get('status')=='SUCCESS':
        return Response({"payment_url":response['GatewayPageURL']})
    return Response({"error":"Payment Initiate Failed"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def payment_success(request):
    tran_id = request.data.get("tran_id")
    if not tran_id:
        return Response({"error": "Transaction ID not provided"}, status=400)

    try:
        purchase_id = tran_id.split('_')[1]
        order = CoursePurchase.objects.get(id=purchase_id)
        order.status = "Paid"
        order.save()
    except (IndexError, CoursePurchase.DoesNotExist):
        return Response({"error": "Invalid transaction or order not found"}, status=404)
    
    return redirect(f"{main_settings.FRONTEND_URL}/dashboard/purchase")

@api_view(['POST'])
def payment_cancel(request):
    return redirect(f"{main_settings.FRONTEND_URL}/dashboard/purchase")

@api_view(['POST'])
def payment_fail(request):
    return redirect(f"{main_settings.FRONTEND_URL}/dashboard/purchase")