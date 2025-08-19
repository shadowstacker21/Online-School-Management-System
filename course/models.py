from django.db import models
from users.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='courses')
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'teacher'},related_name='courses') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)

    def __str__(self):
        return f"{self.title} - {self.teacher.get_full_name()}"
    

class CoursePurchase(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'student'},related_name='purchases')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='purchases')
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student','course')


    def __str__(self):
        return f"{self.student.get_full_name()} bought {self.course.title}"