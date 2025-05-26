from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
from django.utils.html import format_html

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'age_group', 'level', 'price', 'created_at')
    list_filter = (('created_at', JDateFieldListFilter), 'age_group', 'level')
    search_fields = ('title',)

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'created_at')
    list_filter = (('created_at', JDateFieldListFilter), 'course')
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'text', 'created_at')
    list_filter = (('created_at', JDateFieldListFilter), 'course')
    search_fields = ('text', 'user__email')


@admin.register(VocabularyLesson)
class VocabularyLessonAdmin(admin.ModelAdmin):
    list_display = ('word', 'course', 'translation', 'created_at')
    search_fields = ('word', 'translation', 'course__title') 
    list_filter = ('course', 'created_at')
    


@admin.register(ListeningActivity)
class ListeningActivityAdmin(admin.ModelAdmin):
    list_display = ('course', 'season')
    search_fields = ('course__name', 'season__name')
    list_filter = ('course', 'season')
    filter_horizontal = ('audio_files', 'questions', 'images')


@admin.register(ListeningAudio)
class ListeningAudioAdmin(admin.ModelAdmin):
    list_display = ('audio_file',)
    search_fields = ('audio_file',)



@admin.register(ReadingExercise)
class ReadingExerciseAdmin(admin.ModelAdmin):
    list_display = ['course']
    search_fields = ['sentence']
    list_filter = ['course']

@admin.register(WritingTask)
class WritingTaskAdmin(admin.ModelAdmin):
    list_display = ('course', 'sample_text', 'id')
    search_fields = ('course__name',)  
    list_filter = ('course',)  

@admin.register(ConversationPrompt)
class ConversationPromptAdmin(admin.ModelAdmin):
    list_display = ('audio_file','created_at')
    search_fields = ('title',)


class QuestionInline(admin.TabularInline):  
    model = Question.questions.through  
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'season')
    search_fields = ('course__name', 'season__name')  
    filter_horizontal = ('images', 'pdf_files')  
    inlines = [QuestionInline]  


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('text',) 
    search_fields = ('text',) 


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)  
    search_fields = ('image',) 


@admin.register(PdfFile)
class PdfFileAdmin(admin.ModelAdmin):
    list_display = ('file',) 
    search_fields = ('file',) 

class GrammarAudioInline(admin.StackedInline):
    model = GrammarAudio
    extra = 1

@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'season', 'created_at')
    search_fields = ('title',)
    list_filter = ('course', 'season')
    filter_horizontal = ('questions', 'pdf_files')
    inlines = [GrammarAudioInline]

