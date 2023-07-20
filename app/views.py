from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import *

# # Create your views here.
# def insertdummyuser(request):
#     name = "admin"
#     password = "admin"
#     newuser=login.objects.create(name=name,password=password)
#     return render(request,"login.html")

# def validatedata(request):
#     name=request.POST["name"]
#     password=request.POST["password"]
#     data=login.objects.all()
#     for i in data:
#         if i.name == name and i.password == password:
#             ddata =login.objects.all()
#             ddata.delete()
#             return HttpResponse("success")
        
#         elif i.name == name and i.password != password:
#             ddata =login.objects.all()
#             ddata.delete()
#             return render(request,"login.html", {'error_message': 'Invalid password credentials'})
        
#         elif i.name != name and i.password == password:
#             ddata =login.objects.all()
#             ddata.delete()
#             return render(request,"login.html", {'error_message': 'Invalid name credentials'})
#     else:
#         messages.error(request, 'Invalid credentials')
#         return render(request,"login.html", {'error_message': 'Invalid credentials'})

def credential(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        login_obj = login.objects.create(name=name, password=password)
        login_obj.save()
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = login.objects.get(name=username, password=password)

            return redirect('dashboard')
        except:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def dashboard(request):
    return HttpResponse("success")

