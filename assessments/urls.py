from django.urls import path
from .views import *

app_name  = 'assessments'
urlpatterns = [
    path('determine-level/', Determinelevel, name='determine-level'),
    path('get-questions/', GetQuestionsView.as_view(), name='get-questions'),
    path('upload-audio/', UploadAudioView.as_view(), name='upload-audio'),
    path('conversation/', Conversation.as_view(), name='conversation'),
    path('listening/', Listening.as_view(), name='listening'),
    path('question/', Question.as_view(), name='question'),
    path('reading/', Reading.as_view(), name='reading'),
    path('vocabulary/', Vocabulary.as_view(), name='vocabulary'),
    path('writing/', Writing.as_view(), name='writing'),
    path('grammar/', Grammar.as_view(), name='grammar'),
]

