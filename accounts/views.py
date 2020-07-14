from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('user')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,"login.html")




def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"can't use")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                user.save()
        else:
            messages.info(request,"pass not matching")
            return redirect('register')
        return redirect('login')
    else:
        return render(request,"register.html")


def user(request):
    return render(request,'user.html')


'''def user(request):
    from .models import User
    users=User()
    users=User.objects.all()
    p=users[len(users)-1].pic
    return render(request,'user.html',{'users':users})


def upload_image(request):
    from .models import User
    p=request.FILES['image']
    user=User(pic=p)
    user.save()
    print("uploaded")
    return render(request,'user.html')'''