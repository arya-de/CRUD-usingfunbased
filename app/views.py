from django.shortcuts import render,redirect
from .models import student

# Create your views here.




def savestud(request):
    if request.method == 'POST':
        stud = student(fname = request.POST['fname'],
                        lname = request.POST['lname'],
                        age = request.POST['age'],
                        email = request.POST['email'])
        stud.save()
    return render(request,'app/save.html')
    

def studlist(request):
    studt = student.objects.all()
    return render(request,'app/list.html',{'studt':studt})

def delete(request,sid):
    std=student.objects.get(pk=sid)
    std.delete()
    return redirect('/list')


def edit(request,sid):
    studd=student.objects.get(pk=sid)
    return render(request,'app/edit.html',{'studd':studd})

def update(request,sid):
    studt=student.objects.get(pk=sid)
    studt.fname=request.POST.get('fname')
    studt.lname=request.POST.get('lname')
    studt.age=request.POST.get('age')
    studt.email=request.POST.get('email')
    studt.save()
    return redirect('/list')
