from django.shortcuts import render,HttpResponse
from .models import Enquiry,Blog

# Create your views here.

def index(request):
    blog_data = Blog.objects.all()
    context = {
        'Blog':blog_data
    }
    return render(request,'index.html',context)

 
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
    return render(request,'post.html',context)


def postblog(request):
    if request.method == "POST":
        image = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        Blog(image=image,title=title,description=description,date=date).save()
        return HttpResponse("successfully saved!!!!!!")
    return render(request,'postblog.html')





    
