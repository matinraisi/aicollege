from django.contrib import admin
from .models import CustomUser
from django_jalali.admin.filters import JDateFieldListFilter

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'phone', 'role', 'age_group', 'level', 'created_at')
    list_filter = (('created_at', JDateFieldListFilter), 'role', 'age_group', 'level')
    search_fields = ('email', 'first_name', 'phone')
    
    # فارسی کردن عناوین
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'