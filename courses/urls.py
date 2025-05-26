from django.urls import path 
from .views import  CoursListView,Course_Detail


app_name = 'courses'

urlpatterns = [
    path('course/', CoursListView.as_view(), name='course'),
    path('course-detail/<int:pk>/', Course_Detail.as_view(), name='course-detail')
    
]