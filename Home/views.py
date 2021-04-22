from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

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

        Contact.objects.create(name=name , phone=phone, email=email, desc=desc, date=datetime.today())
        messages.success(request,"your message has been sent")
    
    return render(request,"contact.html")

    