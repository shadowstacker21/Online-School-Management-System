from django.shortcuts import render
from course.models import Course,CoursePurchase,Department
from rest_framework.views import APIView
from api.permissions import IsAdminOnlyDashboard
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count,Sum
from rest_framework.response import Response
# Create your views here.

class AdminDashboardView(APIView):
    permission_classes = [IsAdminOnlyDashboard]

    def get(self,request):
        now = timezone.now()
        last_week = now-timedelta(days=7)
        last_month = now-timedelta(days=30)
        current_month_start=now.replace(day=1)
        previous_month_end = current_month_start - timedelta(seconds=1)  
        previous_month_start = previous_month_end.replace(day=1)
        purchase_last_week = CoursePurchase.objects.filter(purchased_at__gte = last_week).count()
        purchase_last_month = CoursePurchase.objects.filter(purchased_at__gte=last_month).count()

        most_purchased_course = CoursePurchase.objects.values('course__title').annotate(total=Count('course')).order_by('-total')[:5]

        most_buy_student = CoursePurchase.objects.values('student__id','student__email').annotate(total=Count('id')).order_by('-total')[:5]

        current_month_sale = CoursePurchase.objects.filter(
            purchased_at__gte =previous_month_start
                                                            
        ).aggregate(total=Sum('course__price'))['total'] or 0


        previous_month_sale = CoursePurchase.objects.filter(
            purchased_at__gte =previous_month_start,
            purchased_at__lt = current_month_start
        ).aggregate(total=Sum('course__price'))['total'] or 0

        return Response(
           {
               " purchase_last_week":purchase_last_week,
                "purchase_last_month":purchase_last_month,
                "most_purchased_course":most_purchased_course,
               " most_buy_student":most_buy_student,
               "Sales":{
                   "current_month_sale":current_month_sale,
                   "previous_month_sale":previous_month_sale
               }
           }

        )