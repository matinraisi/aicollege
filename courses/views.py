from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Course
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.

class CoursListView(View):
    template_name = 'courses/course.html'
    def get(self, request):
        courses = Course.objects.all().order_by('-created_at')  # ترتیب از جدید به قدیم
        context = {
            'courses': courses
        }
        return render(request, self.template_name, context)
    

@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class Course_Detail(View):
    template_name = 'courses/course-detail.html'
    def get(self, request,pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, self.template_name,{'course':course})

