import random

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm, EmailVerificationForm
from users.models import User, UserVerification


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:send_verification_email')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verify(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        user_verification = UserVerification.objects.get(verification_code=verification_code)
        user_verification.is_verified = True
        user_verification.save()
        return redirect('/')
    else:
        return render(request, 'verification/verify.html')


def send_verification_email(request):
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            verification_code = str(random.randint(100000, 999999))
            UserVerification.objects.create(user=user, verification_code=verification_code)
            send_mail(
                'Verification code',
                f'Ваш код для авторизации {verification_code}',
                'margoonavt@yandex.ru',
                [email],
                fail_silently=False,
            )
            return redirect('users:verify')
    else:
        form = EmailVerificationForm()
    return render(request, 'verification/send_verification_email.html', {'form': form})


