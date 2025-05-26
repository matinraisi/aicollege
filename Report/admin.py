from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserPronunciation)
class UserPronunciationAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'is_correct', 'attempt_number', 'timestamp')
    list_filter = ('is_correct', 'attempt_number', 'timestamp')
    search_fields = ('user__username', 'word__word')

@admin.register(ListeningAnswer)
class ListeningAnswerAdmin(admin.ModelAdmin):
    list_display = ('activity', 'user', 'submitted_at')
    list_filter = ('activity', 'submitted_at')
    search_fields = ('user__email', 'activity__title', 'answer1', 'answer2', 'answer3')

@admin.register(ReadingSubmission)
class ReadingSubmissionAdmin(admin.ModelAdmin):
    list_display = ['user', 'exercise', 'submitted_at']
    search_fields = ['user__username', 'exercise__sentence']
    list_filter = ['submitted_at', 'exercise__course']


@admin.register(ConversationResponse)
class ConversationResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'prompt', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('user__username', 'prompt__title')

admin.site.register(Answer)


@admin.register(UserWritingTask)
class UserWritingTaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'writing_task', 'submitted_at', 'id')
    search_fields = ('user__username', 'writing_task__course__name')  
    list_filter = ('user', 'writing_task__course')  

@admin.register(GrammarAnswer)
class GrammarAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'grammar', 'question', 'is_correct', 'submitted_at')
    list_filter = ('is_correct', 'submitted_at', 'grammar')
    search_fields = ('user__username', 'user__email', 'question__title', 'user_answer')
    ordering = ('-submitted_at',)