from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# این کلاس برای مدیریت کاربران سفارشی است
class CustomUserManager(BaseUserManager):
    # متد ایجاد کاربر عادی
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('ایمیل اجباری است!')
        email = self.normalize_email(email) # نرمال‌سازی ایمیل
        extra_fields.setdefault('is_active', True) # کاربر به صورت پیش‌فرض فعال است
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # رمز عبور را هش می‌کند
        user.save(using=self._db)
        return user

    # متد ایجاد ادمین
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) # دسترسی به پنل ادمین
        extra_fields.setdefault('is_superuser', True) # دسترسی‌های کامل
        extra_fields.setdefault('role', 'admin') # نقش ادمین
        return self.create_user(email, password, **extra_fields)

# مدل اصلی کاربر سفارشی
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # تعریف انواع نقش‌های کاربری
    ROLES = (
        ('student', 'دانشجو'),
        ('instructor', 'مدرس'),
        ('admin', 'ادمین'),
    )
    # تعریف گروه‌های سنی
    AGE_GROUPS = (
        ('child', 'کودک'),
        ('teen', 'نوجوان'),
        ('adult', 'بزرگسال'),
    )
    # تعریف سطوح آموزشی
    LEVELS = (
        ('beginner', 'مبتدی'),
        ('intermediate', 'متوسط'),
        ('advanced', 'پیشرفته'),
    )

    # فیلدهای مدل کاربر
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name='شماره تلفن')
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام خانوادگی')
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name='سن')
    age_group = models.CharField(max_length=10, choices=AGE_GROUPS, blank=True, verbose_name='گروه سنی')
    level = models.CharField(max_length=20, choices=LEVELS, blank=True, verbose_name='سطح')
    role = models.CharField(max_length=20, choices=ROLES, default='student', verbose_name='نقش')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت‌نام')

    USERNAME_FIELD = 'email' # فیلد نام کاربری، ایمیل است
    REQUIRED_FIELDS = [] # فیلدهای اجباری

    objects = CustomUserManager() # استفاده از منیجر سفارشی

    # متد ذخیره‌سازی با منطق اضافه
    def save(self, *args, **kwargs):
        # تعیین خودکار گروه سنی بر اساس سن
        if self.age is not None:
            if self.age < 13:
                self.age_group = 'child'
            elif 13 <= self.age <= 18:
                self.age_group = 'teen'
            else:
                self.age_group = 'adult'
        # اعطای دسترسی‌های ادمین
        if self.role == 'admin':
            self.is_staff = True
            self.is_superuser = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    # تنظیمات متا برای مدل
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'