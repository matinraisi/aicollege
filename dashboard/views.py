from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from courses.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import UserCourse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib import messages
from accounts.models import CustomUser
# Create your views here.



class Student_bookmark(View):
    template_name = 'dashboard/student-bookmark.html'
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(request, self.template_name,context)
    
class Student_Dashboard(LoginRequiredMixin, View):
    template_name = 'dashboard/student-dashboard.html'

    def get(self, request):
        user_courses = UserCourse.objects.filter(user=request.user).select_related('course')
        return render(request, self.template_name, {
            'user_courses': user_courses
        })
    def post(self, request):
        course_id = request.POST.get('delete_course_id')
        if course_id:
            uc = get_object_or_404(UserCourse, id=course_id, user=request.user)
            uc.delete()
        return redirect('dashboard:student-dashboard')
    

class Student_Edit_Profile(LoginRequiredMixin, View):
    template_name = 'dashboard/student-edit-profile.html'

    def get(self, request):
        return render(request, self.template_name, {
            'user': request.user
        })

    def post(self, request):
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.phone = request.POST.get('phone', user.phone)
        # user.education = request.POST.get('education', user.education)  # اگر همچین فیلدی در مدل داری
        
        user.save()
        messages.success(request, "پروفایل با موفقیت ویرایش شد.")
        return redirect('dashboard:student-edit-profile')  # به آدرس درست خودت هدایت کن
    

class Dashboard_Lesson(View):
    template_name = 'dashboard/dashboard-lesson.html'

    def get(self, request, pk):
        # فقط اگر کاربر دوره را خریده باشد، نمایش داده شود
        user_course = get_object_or_404(UserCourse, user=request.user, course_id=pk)
        course = user_course.course
        seasons = course.seasons.all()  # گرفتن فصل‌های مرتبط با این دوره

        
        context = {
            'course': course,
            'seasons': seasons,
        }
        return render(request, self.template_name, context)
    
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
        user_courses = UserCourse.objects.filter(user=request.user)
        return render(request, self.template_name ,{'courses': user_courses})
    

    
class Student_Quiz(View):
    template_name = 'dashboard/student-quiz.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Student_Subscription(View):
    template_name = 'dashboard/student-subscription.html'
    def get(self, request):
        return render(request, self.template_name)
    

class Lesson(View):
    template_name = 'dashboard/lesson.html'
    def get(self, request):
        return render(request, self.template_name)