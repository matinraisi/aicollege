python manage.py startapp accounts
python manage.py startapp assessments
python manage.py startapp courses
python manage.py startapp conversations


smart_college/
│
├── templates/
│   ├── base.html   # تمپلیت اصلی
│   ├── navbar.html
│   ├── footer.html
│
│   ├── accounts/
│   │   └── login.html
│   │   └── register.html
│
│   ├── courses/
│   │   └── course_list.html
│   │   └── course_detail.html
│
│   ├── assessments/
│   │   └── quiz.html
│
│   └── conversations/
│       └── chat.html