from django.shortcuts import render
from django.views import View
from courses.models import Course


# Create your views here.



class Student_bookmark(View):
    template_name = 'dashboard/student-bookmark.html'
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }

        return render(request, self.template_name,context)
    
class Student_Dashboard(View):
    template_name = 'dashboard/student-dashboard.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Student_Course_Delete_Account(View):
    template_name = 'dashboard/student-course-delete-account.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Student_Course_List(View):    
    template_name = 'dashboard/student-course-list.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Student_Course_Resume(View):
    template_name = 'dashboard/student-course-resume.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Student_Edit_Profile(View):
    template_name = 'dashboard/student-edit-profile.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Student_Quiz(View):
    template_name = 'dashboard/student-quiz.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Student_Subscription(View):
    template_name = 'dashboard/student-subscription.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Dashboard_Lesson(View):
    template_name = 'dashboard/dashboard-lesson.html'
    def get(self, request):
        return render(request, self.template_name)
    

class Lesson(View):
    template_name = 'dashboard/lesson.html'
    def get(self, request):
        return render(request, self.template_name)