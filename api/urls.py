from django.urls import path,include
from users.views import ChangeUserRoleView
from rest_framework_nested import routers
from course.views import CourseViewSet,DepartmentView

router = routers.DefaultRouter()
router.register('user',ChangeUserRoleView,basename='users')
router.register('courses',CourseViewSet,basename='course')
router.register('departments',DepartmentView,basename='department')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
]
