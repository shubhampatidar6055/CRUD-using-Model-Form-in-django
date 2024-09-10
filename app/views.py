from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method == "POST":
        data = StudentRegistration(request.POST)
        if data.is_valid():
            nm = data.cleaned_data['name']
            em = data.cleaned_data['email']
            pw = data.cleaned_data['password']
        reg = Student(name=nm, email=em, password=pw)
        reg.save()
        return redirect("/")
    else:
        data = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'index.html', {"form":data, "stud":stud})

def update(request, pk):
    if request.method == "POST":
        obj = Student.objects.get(id=pk)
        data = StudentRegistration(request.POST, instance=obj)
        if data.is_valid():
            data.save()
    else:
        obj = Student.objects.get(id=pk)
        data = StudentRegistration(instance=obj)
    return render(request, 'update.html', {"form":data})

def delete(request, pk):
    if request.method == "POST":
        obj = Student.objects.get(id=pk)
        obj.delete()
        return redirect("/")