from django.db import models
from accounts.models import CustomUser
from courses.models import *
# Create your models here.

#پاسخ لغت 
class UserPronunciation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر',null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه',default="")
    word = models.ForeignKey(VocabularyLesson, on_delete=models.CASCADE, verbose_name="لغت")
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    pronunciation_audio = models.FileField("فایل تلفظ", upload_to='pronunciations/')
    is_correct = models.BooleanField("تلفظ صحیح بود؟")
    attempt_number = models.IntegerField("شماره تلاش", default=1)
    timestamp = models.DateTimeField("زمان ثبت", auto_now_add=True)

    class Meta:
        verbose_name = "تلفظ کاربر"
        verbose_name_plural = "لغت های کاریر"

    def __str__(self):
        return f"{self.word.word} - تلاش {self.attempt_number}"


# پاسخ‌های هر کاربر ذخیره می‌شن
#پاسخ های درس شنیداری
class ListeningAnswer(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه',default="")
    activity = models.ForeignKey(ListeningActivity,on_delete=models.CASCADE,verbose_name='تمرین مربوطه')
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name='کاربر', blank=True,null=True)
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    answers = models.TextField("پاسخ‌ها", help_text="تمامی پاسخ‌ها در یک فیلد به صورت جداگانه وارد میشوند.",default="")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال')

    class Meta:
        verbose_name = 'پاسخ تمرین شنیداری'
        verbose_name_plural = 'پاسخ‌های تمرین شنیداری'


#پاسخ تمرین روخوانی 
class ReadingSubmission(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه',default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    exercise = models.ForeignKey(ReadingExercise, on_delete=models.CASCADE, verbose_name='تمرین')
    audio_file = models.FileField(upload_to='reading_audios/', verbose_name='فایل صوتی ضبط‌شده')
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name = 'پاسخ تمرین روخوانی'
        verbose_name_plural = 'ارسال‌های تمرین روخوانی'
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.exercise} - {self.submitted_at.strftime('%Y-%m-%d')}"
    

class UserWritingTask(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه',default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر', null=True, blank=True)
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    writing_task = models.ForeignKey(WritingTask, on_delete=models.CASCADE, verbose_name="تمرین نوشتاری")
    user_text = models.TextField(verbose_name="متن نوشته شده توسط کاربر", blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "تمرین نوشتاری کاربر"
        verbose_name_plural = "تمرین‌های نوشتاری کاربران"

class ConversationResponse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    prompt = models.ForeignKey(ConversationPrompt, on_delete=models.CASCADE, verbose_name='مکالمه مربوطه')
    user_audio = models.FileField(upload_to='user_conversations/', verbose_name="فایل صوتی کاربر")
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پاسخ مکالمه معلم"
        verbose_name_plural = "پاسخ‌های مکالمه"

    def __str__(self):
        return str(self.user)
    
class Answer(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name='درس مرتبط', null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answers = models.TextField("پاسخ‌ها", help_text="تمامی پاسخ‌ها در یک فیلد به صورت جداگانه وارد میشوند.")
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پاسخ سوالات"
        verbose_name_plural = "پاسخ‌ سوالات"

    def __str__(self):
        return f"پاسخ‌نامه {self.id} - {self.user if self.user else 'کاربر'}"
    
class GrammarAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    grammar = models.ForeignKey('courses.Grammar', on_delete=models.CASCADE, verbose_name='گرامر مربوطه')
    question = models.ForeignKey('courses.Questions', on_delete=models.CASCADE, verbose_name='سؤال')
    user_answer = models.TextField(verbose_name='پاسخ کاربر')
    is_correct = models.BooleanField(verbose_name='پاسخ صحیح است؟', default=False)
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    
    class Meta:
        verbose_name = 'پاسخ گرامر'
        verbose_name_plural = 'پاسخ گرامر'
        
    def __str__(self):
        return f"{self.user} - {self.question} - {'✔' if self.is_correct else '✘'}"