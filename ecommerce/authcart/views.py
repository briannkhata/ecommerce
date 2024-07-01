from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token
# from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError

from django.core.mail import EmailMessage
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if (password != confirm_password):
            messages.warning(request, "Passwords Do Not Match!")
            return render(request, 'authentication/signup.html')

        try:
            if User.objects.get(username=email):
                messages.info(request, "Email already Exists!")
                return render(request, 'authentication/signup.html')
        except Exception as e:
            pass

        user = User.objects.create_user(email, email, password)
        user.is_active = False
        user.save()

        email_subject = "Activate Your Account"
        message = render_to_string('authentication/activate.html', {
            'user': user,
            'domain': '127.0.0.1:7000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
        email_message.send()
        messages.info(request, "Activate Your Account by clicking the link in your email!")
        return redirect(request, 'auth/login/')
    else:
        return render(request, 'authentication/signup.html')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.info(request, "Account Activated Successfully")
            return redirect('/auth/login')
        return render(request, 'authentication/activatefail.html')


def handlelogin(request):
    return render(request, 'authentication/login.html')


def handlelogout(request):
    return redirect("/authcart/login")
