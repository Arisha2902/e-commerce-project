from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method  == "POST":
        email= request.POST['email']
        password= request.POST['pass1']
        confirm_password= request.POST['pass2']
        if password !=confirm_password:
            messages.warning(request, " Password is not matching")
            return render(request, 'signup.html')
            return HttpResponse("password incorrectt")
        
        
        try:
            if User.objects.get(username=email):
              return  HttpResponse("email already exist ")

                # return render(request, 'auth/signup.html')
            
        except Exception as identifiers:
            pass
        user = User.objects.create_user( email,email,password)
        user.save()
        return HttpResponse("user created")

    return render(request, "signup.html")

def handlelogin(request):
    return render(request, "login.html")

def handlelogout(request):
    return redirect('/auth/login')
    # return render(request, "authentication/signup.html")

