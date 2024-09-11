from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Enquiry,Blog


# Create your views here.

def index(request):
    blog_data = Blog.objects.all()
    context = {
        'Blog':blog_data
    }
    return render(request,'rightside.html',context)

 
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Enquiry(name=name,email=email,subject=subject,message=message).save()
        return HttpResponse("successfully saved!!!!!!")
    return render(request,'contact.html')

def post(request,id):
     
    post_data = Blog.objects.filter(id=id)
    context = {
    'mainblog':post_data[0]
    }
    return render(request,'postblog.html',context)


def postblog(request):
    if request.method == "POST":
        image = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        Blog(image=image,title=title,description=description,date=date).save()
        return HttpResponse("successfully saved!!!!!!")
    return render(request,'postblog.html')


def loginhandle(request):
    if request.method =="POST":
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        
        else:
            messages.success(request,"user not found.....")
    return render(request,'login.html')

def signuphandle(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        user = User(username=name,email=email)
        if (password==confirm_password):
            user.set_password(password)
            user.save()
            messages.success(request,"your Account Successfully created")
        else:
            messages.success(request,"Both Field should be same")  
    return render(request,'signup.html')


def logouthandle(request):
    logout(request)
    return redirect('/login/')



    
