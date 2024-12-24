from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token 
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method  == "POST":
        email= request.POST['email']
        password= request.POST['pass1']
        confirm_password= request.POST['pass2']
        if password !=confirm_password:
            messages.warning(request, " Password is not matching")
            return render(request, 'signup.html')
        try:
            if User.objects.get(username=email):
                messages.warning(request, " Email is taken")
                return render(request, 'signup.html')
                 
            #   return  HttpResponse("email already exist ")
        except Exception as identifiers:
            pass
        user = User.objects.create_user( email,email,password)
        user.is_active = False
        user.save()
        email_subject = "Activate your account"
        message = render_to_string( 'activate.html', {
            'user': user,
            # 'domain': get_current_site(request).domain,
            'domain': '127.0.0.1:8000' ,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)

        })

        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request, "Activate your account by clicking on the link sent to your email") 
        return redirect('/auth/login')

    return render(request, "signup.html")


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            user.save()
            messages.info(request, "Account activated successfully")
            return redirect('/authen/login')
        return redirect(request, 'auth/actiavtefail.html')

def handlelogin(request):
    return render(request, "login.html")

def handlelogout(request):
    return redirect('/auth/login')
    # return render(request, "authentication/signup.html")

