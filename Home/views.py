from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1": "hii my name is ankit",
        "variable2": "hii my name is anii",
        "variable3": "hii my name is neetu"
    }
    
    return render(request, "index.html",context)
    #return HttpResponse("this is homepage")
def about(request):
    return render(request, "about.html")

    #return HttpResponse("this is about page")

def audio(request):
    return render(request, "audio.html")

def video(request):
    return render(request, "video.html")

def photo(request):
    return render(request, "photo.html")

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')

        
        contact = Contact(name=name , phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,"your message has been sent")
    
    return render(request,"contact.html")

    