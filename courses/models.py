from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Course(models.Model):
    AGE_GROUPS = (
        ('child', 'کودک'),
        ('teen', 'نوجوان'),
        ('adult', 'بزرگسال'),
    )
    LEVELS = (
        ('beginner', 'مبتدی'),
        ('intermediate', 'متوسط'),
        ('advanced', 'پیشرفته'),
    )
    LANGUAGES = (
    ('english', 'انگلیسی'),
    ('french', 'فرانسوی'),
    ('german', 'آلمانی'),
    ('arabic', 'عربی'),
)
    CERTIFICATE_STATUS = (
    ('yes', 'دارد'),
    ('no', 'ندارد'),
    ('pending', 'در حال بررسی'),
)
    title = models.CharField(max_length=200, verbose_name='عنوان')
    age_group = models.CharField(max_length=10, choices=AGE_GROUPS, verbose_name='گروه سنی')
    level = models.CharField(max_length=20, choices=LEVELS, verbose_name='سطح')
    language = models.CharField(max_length=20, choices=LANGUAGES, verbose_name='زبان دوره', default='english')
    certificate_status = models.CharField(max_length=10,choices=CERTIFICATE_STATUS,verbose_name='وضعیت مدرک',default='yes')
    lesson_count = models.PositiveIntegerField(default=0, verbose_name='تعداد درس')
    time_duration = models.DecimalField(max_digits=4,decimal_places=1,verbose_name='مدت زمان دوره (ساعت)',default=0)
    poster = models.ImageField(upload_to='posters/', verbose_name='پوستر', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت (تومان)')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره‌ها'

class Season(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='seasons', verbose_name='دوره')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    order = models.PositiveIntegerField(default=1, verbose_name='ترتیب')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'درس ها'
        ordering = ['order']


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', verbose_name='دوره')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    text = models.TextField(verbose_name='متن')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name='پاسخ به')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')

    def __str__(self):
        return f"{self.user.email} - {self.text[:50]}"

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت‌ها'
        ordering = ['-created_at']



#اموزش لغت 
class VocabularyLesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='vocab_lessons',verbose_name='دوره مرتبط')
    season = models.ForeignKey(Season,on_delete=models.CASCADE,related_name='vocab_lessons',verbose_name='درس مرتبط',default="")
    word = models.CharField(max_length=100, verbose_name='لغت')
    image = models.ImageField("تصویر", upload_to='words/')
    translation = models.CharField("ترجمه فارسی", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'درس لغت'
        verbose_name_plural = 'درس‌ لغت'

#بخش شنیداری
class ListeningActivity(models.Model):
    season = models.ForeignKey('Season', on_delete=models.CASCADE, verbose_name='درس مرتبط')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    audio_files = models.ManyToManyField('ListeningAudio', blank=True, related_name='listening_activities', verbose_name='فایل‌های صوتی')
    questions = models.ManyToManyField('Questions',  blank=True, related_name='listening_activity_questions', verbose_name='سوالات')
    images = models.ManyToManyField('Image', blank=True, related_name='listening_activity_images', verbose_name='تصاویر')
    class Meta:
        verbose_name = 'تمرین شنیداری'
        verbose_name_plural = 'تمرین‌های شنیداری'

    def __str__(self):
        return f"شنیداری دوره: {self.course} - درس: {self.season}"

#تمرین روخوانی
class ReadingExercise(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    sentence = models.TextField(max_length=500,verbose_name='متن روخوانی')
    images = models.ManyToManyField('Image', blank=True, related_name='Readin_activity_imagesns', verbose_name='تصاویر')
    pdf_files = models.ManyToManyField('PdfFile', blank=True, related_name='Readin_activity_questions', verbose_name='فایل‌های PDF')

    class Meta: 
        verbose_name = 'تمرین روخوانی'
        verbose_name_plural = 'تمرین‌های روخوانی'
        ordering = ['-id']

    def __str__(self):
        return f"{self.course} - {self.sentence[:30]}"


#نوشتاری 
class WritingTask(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    sample_text = models.TextField(verbose_name="متن نمونه توسط ادمین")
    images = models.ManyToManyField('Image', blank=True, related_name='WritingTask', verbose_name='تصاویر')
    pdf_files = models.ManyToManyField('PdfFile', blank=True, related_name='WritingTask_questions', verbose_name='فایل‌های PDF')

    class Meta:
        verbose_name = "تمرین نوشتاری"
        verbose_name_plural = "تمرین‌های نوشتاری"

    #مکالمه 
class ConversationPrompt(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    season = models.ForeignKey(Season,on_delete=models.CASCADE,verbose_name='درس مرتبط',default="")
    audio_file = models.FileField(upload_to='conversation_prompts/', verbose_name="فایل معلم")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "مکالمه معلم"
        verbose_name_plural = "مکالمه‌های معلم"
#پرسش و پاسخ 
class Question(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, verbose_name='درس مربوطه')
    questions = models.ManyToManyField('Questions',  blank=True, related_name='questions', verbose_name='سوالات')
    images = models.ManyToManyField('Image', blank=True, related_name='questions', verbose_name='تصاویر')
    pdf_files = models.ManyToManyField('PdfFile', blank=True, related_name='questions', verbose_name='فایل‌های PDF')

    class Meta:
        verbose_name = "سؤال"
        verbose_name_plural = " پرسش سؤالات"

    def __str__(self):
        return f"سوالات دوره: {self.course} - درس: {self.season}"
    

#گرامر 
class Grammar(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='دوره مربوطه')
    season = models.ForeignKey('Season', on_delete=models.CASCADE, verbose_name='درس مربوطه')
    title = models.CharField(max_length=255, verbose_name='عنوان گرامر')
    questions = models.ManyToManyField('Questions',blank=True, related_name='grammars', verbose_name='سوالات')
    pdf_files = models.ManyToManyField('PdfFile', blank=True, related_name='grammars', verbose_name='فایل‌های PDF')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "گرامر"
        verbose_name_plural ="گرامر ها" 

    def __str__(self):
        return f"Grammar: {self.title}"

    

class Image(models.Model):
    image = models.ImageField(upload_to='question_images/', verbose_name='تصویر')

    def __str__(self):
        return str(self.image)
    
class Questions(models.Model):
    text = models.TextField(max_length=500, verbose_name='سوال')

    def __str__(self):
        return str(self.text)


class PdfFile(models.Model):
    file = models.FileField(upload_to='question_pdfs/', verbose_name='فایل PDF')

    def __str__(self):
        return str(self.file)
    
class ListeningAudio(models.Model):
    audio_file = models.FileField(upload_to='listening_audios/', verbose_name='فایل صوتی')

    def __str__(self):
        return str(self.audio_file)
    
class GrammarAudio(models.Model):
    grammar = models.ForeignKey('Grammar', on_delete=models.CASCADE, related_name='audio_files', verbose_name='گرامر',default='')
    file = models.FileField(upload_to='grammar/audio/', verbose_name='فایل صوتی')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name 

    