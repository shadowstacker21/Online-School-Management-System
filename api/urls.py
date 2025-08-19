from django.urls import path,include
from users.views import ChangeUserRoleView
from rest_framework_nested import routers
from course.views import CourseViewSet,DepartmentView,CoursePurchaseView
from api.views import AdminDashboardView

router = routers.DefaultRouter()
router.register('user',ChangeUserRoleView,basename='users')
router.register('courses',CourseViewSet,basename='course')
router.register('departments',DepartmentView,basename='department')

purchase_router = routers.NestedDefaultRouter(router,'courses',lookup='course')
purchase_router.register('purchases',CoursePurchaseView,basename='purchase')

urlpatterns = [
    path('', include(router.urls)),
    path('',include(purchase_router.urls)),
    path('admin-dashboard/',AdminDashboardView.as_view(),name='admin-dashboard'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
]
