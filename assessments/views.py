from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question, UserAnswer
from django.urls import reverse_lazy
# from transformers import pipeline


@login_required(login_url=reverse_lazy('accounts:login'))
def Determinelevel(request):
    return render(request, 'assessments/Determinelevel.html')


class GetQuestionsView(View):
    def get(self, request):
        questions = Question.objects.all()
        data = [
            {
                'id': q.id,
                'text': q.text,
                'level': q.level
            }
            for q in questions
        ]
        return JsonResponse({'questions': data})


@method_decorator(csrf_exempt, name='dispatch')
class UploadAudioView(View):
    def post(self, request):
        audio_file = request.FILES.get('audio')
        question_id = request.POST.get('question_id')

        # چک می‌کنیم که آیا کاربر قبلاً برای این سوال جواب داده یا نه
        existing_answer = UserAnswer.objects.filter(user=request.user, question_id=question_id).first()

        if existing_answer:
            # اگر جواب قبلی وجود داشت، فایل صوتی رو آپدیت کن
            existing_answer.audio_response = audio_file
            existing_answer.save()
        else:
            # اگر جوابی وجود نداشت، جواب جدید بساز
            UserAnswer.objects.create(
                user=request.user,
                question_id=question_id,
                audio_response=audio_file
            )

        return JsonResponse({'message': 'Audio uploaded successfully'})

class Conversation(View):
    template_name = 'lesson/conversation.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Listening(View):
    template_name = 'lesson/listening.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Reading(View):
    template_name = 'lesson/reading.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Vocabulary(View):
    template_name = 'lesson/vocabulary.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Writing(View):
    template_name = 'lesson/writing.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Question(View):
    template_name = 'lesson/question.html'
    def get(self, request):
        return render(request, self.template_name)
    
class Grammar(View):
    template_name = 'lesson/grammar.html'
    def get(self, request):
        return render(request, self.template_name)