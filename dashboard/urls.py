from django.urls import path
from .views import Student_bookmark,Student_Dashboard,Student_Course_Delete_Account,Student_Course_List,Student_Course_Resume,Student_Edit_Profile,Student_Quiz,Student_Subscription,Dashboard_Lesson,Lesson

app_name = 'dashboard'

urlpatterns = [
    path('student-bookmark/', Student_bookmark.as_view(), name='student-bookmark'),
    path('student-dashboard/', Student_Dashboard.as_view(), name='student-dashboard'),
    path('student-course-delete-account/', Student_Course_Delete_Account.as_view(), name='student-course-delete-account'),
    path('student-course-list/', Student_Course_List.as_view(), name='student-course-list'),    
    path('student-course-resume/', Student_Course_Resume.as_view(), name='student-course-resume'),
    path('student-edit-profile/', Student_Edit_Profile.as_view(), name='student-edit-profile'),
    path('student-quiz/', Student_Quiz.as_view(), name='student-quiz'),
    path('student-subscription/', Student_Subscription.as_view(), name='student-subscription'),
    path('dashboard-lesson/<int:pk>/', Dashboard_Lesson.as_view(), name='dashboard-lesson'),
    path('lesson',Lesson.as_view(), name='lesson')
    
]
