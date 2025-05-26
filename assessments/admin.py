from django.contrib import admin
from .models import Question, UserAnswer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'text', 'level')  
    list_filter = ('level',)
    search_fields = ('text',)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'audio_response', 'is_correct')
