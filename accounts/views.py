from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

CustomUser = get_user_model()

class SignUpView(View):
    template_name = 'accounts/sign-up.html'

    def post(self, request):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # اعتبارسنجی
        if not email or not phone or not age or not password or not confirm_password:
            return render(request, self.template_name, {'error': 'لطفاً تمام فیلدها را پر کنید!'})

        try:
            validate_email(email)
        except ValidationError:
            return render(request, self.template_name, {'error': 'ایمیل معتبر نیست!'})

        if CustomUser.objects.filter(email=email).exists():
            return render(request, self.template_name, {'error': 'این ایمیل قبلاً ثبت شده است!'})

        if CustomUser.objects.filter(phone=phone).exists():
            return render(request, self.template_name, {'error': 'شماره تلفن قبلاً ثبت شده است!'})

        try:
            age = int(age)
            if age < 5:
                return render(request, self.template_name, {'error': 'سن وارد شده معتبر نیست!'})
        except ValueError:
            return render(request, self.template_name, {'error': 'سن باید به صورت عدد باشد!'})

        if password != confirm_password:
            return render(request, self.template_name, {'error': 'رمز عبور و تایید رمز یکسان نیست!'})

        if len(password) < 4:
            return render(request, self.template_name, {'error': 'رمز عبور باید حداقل 8 کاراکتر باشد!'})

        # ثبت نام کاربر
        try:
            CustomUser.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                age=age,
                password=make_password(password)
            )
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
            return redirect('core:home')
        except Exception as e:
            return render(request, self.template_name, {'error': f'خطا در ثبت نام: {str(e)}'})

    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'accounts/sign-in.html'

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, self.template_name, {'error': 'لطفاً ایمیل و رمز عبور را وارد کنید!'})

        user = authenticate(request, email=email, password=password)
        if user is None:
            return render(request, self.template_name, {'error': 'ایمیل یا رمز عبور اشتباه است!'})

        login(request, user)
        return redirect('core:home')  # بعد از لاگین به صفحه اصلی

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')
