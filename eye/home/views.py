from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models

# Create your views here.


def home(request):
    return render(request, 'index.html')

def appplication(request):
    return render(request, 'application.html')

def saveFeedback(request):
    if request.method=='POST':
            name100 = request.POST['name100']
            email100 = request.POST['email100']
            phonenumber100 = request.POST['phonenumber100']
            feedback100 = request.POST['feedback100']
            ins = models.Feedback(name100=name100, email100=email100, phonenumber100=phonenumber100, feedback100=feedback100)
            ins.save()
    return render(request, 'index.html')


def signUp(request):
    if request.method=='POST':
            name20 = request.POST['name20']
            username20 = request.POST['username20']
            password20 = request.POST['password20']
            phonenumber20 = request.POST['phonenumber20']
            email20 = request.POST['email20']
            name30 = request.POST['name30']
            phonenumber30 = request.POST['phonenumber30']
            name40 = request.POST['name40']
            phonenumber40 = request.POST['phonenumber40']
            ins = models.Signup(name20=name20, username20=username20, password20=password20, phonenumber20 = phonenumber20, email20=email20, 
                                name30 = name30, phonenumber30 = phonenumber30, name40 = name40, phonenumber40=phonenumber40)
            ins.save()
    return render(request, 'application.html')


def login(request):
    print('called me')
    if request.method=='POST':
        username10 = request.POST['username10']
        password10 = request.POST['password10']
        if models.Signup.objects.filter(username20=username10, password20=password10):
            return render(request, 'application.html')
        else:
            return render(request, 'index.html')

def logout(request):
    return render (request, 'index.html')
         

def about(request):
    return render(request, 'about.html')