from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Course,UserCourse
from assessments.models import UserAnswer  # این خط را اضافه کن
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.

class CoursListView(View):
    template_name = 'courses/course.html'

    def get(self, request):
        courses = Course.objects.all().order_by('-created_at')  # ترتیب از جدید به قدیم
        has_taken_level_test = False
        if request.user.is_authenticated:
            has_taken_level_test = UserAnswer.objects.filter(user=request.user).exists()
        context = {
            'courses': courses,
            'has_taken_level_test': has_taken_level_test,
        }
        return render(request, self.template_name, context)
    

@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class Course_Detail(View):
    template_name = 'courses/course-detail.html'

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, self.template_name, {'course': course})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        user = request.user

        # اگر کاربر قبلا این دوره رو نخریده، ثبتش کن
        if not UserCourse.objects.filter(user=user, course=course).exists():
            UserCourse.objects.create(user=user, course=course)
        
        # بعد به داشبورد کاربر هدایتش کن
        return redirect('dashboard:student-dashboard')
