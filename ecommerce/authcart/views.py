from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


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
                messages.warning(request, "Eamil already Exists!")
                return render(request, 'authentication/signup.html')
        except Exception as e:
            pass
        user = User.objects.create_user(email, email, password)
        user.save()
        return render(request, 'authentication/signup.html')
    else:
        print("get")
    return render(request, 'authentication/signup.html')


def handlelogin(request):
    return render(request, 'authentication/login.html')


def handlelogout(request):
    return redirect("/authcart/login")
