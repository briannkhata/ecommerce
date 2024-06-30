from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if (password != confirm_password):
            return HttpResponse("Password do not match")
            # return render(request,'auth/signup.html')

        try:
            if User.objects.get(username=email):
                return HttpResponse("Email already exists")
                # return render(request, 'auth/signup.html')
        except Exception as e:
            pass
        user = User.objects.create_user(email, email, password)
        user.save()
        return HttpResponse("User Created", email)
    else:
        print("get")
    return render(request, 'authentication/signup.html')


def handlelogin(request):
    return render(request, 'authentication/login.html')


def handlelogout(request):
    return redirect("/authcart/login")
