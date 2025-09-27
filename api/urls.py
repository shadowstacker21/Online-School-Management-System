from django.urls import path,include
from users.views import ChangeUserRoleView
from rest_framework_nested import routers
from course.views import TeacherCourseView,CourseViewSet,payment_cancel,payment_fail,payment_success,my_purchases,payment_initiate,DepartmentView,CoursePurchaseView
from api.views import AdminDashboardView
router = routers.DefaultRouter()
router.register('user',ChangeUserRoleView,basename='users')
router.register('courses',CourseViewSet,basename='course')
router.register('departments',DepartmentView,basename='department'),
router.register('teacher_courses',TeacherCourseView,basename="teacher_courses"),
purchase_router = routers.NestedDefaultRouter(router,'courses',lookup='course')
purchase_router.register('purchases',CoursePurchaseView,basename='purchase')

urlpatterns = [
    path('', include(router.urls)),
    path('',include(purchase_router.urls)),
    path('admin-dashboard/',AdminDashboardView.as_view(),name='admin-dashboard'),
     path('payment/initiate/',payment_initiate,name='payment-initiate'),
     path('my-purchases/', my_purchases, name='my-purchases'),
    path("payment/success/",payment_success,name="payment-success"),
    path("payment/cancel/",payment_cancel,name="payment-cancel"),
    path("payment/fail/",payment_fail,name="payment-fail"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

   
    
]
