
from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
def index(request):
    course = courses.objects.all()
    context = {
        'courses': course
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        errors = courses.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
         newcour = courses.objects.create(
        name=request.POST['name'],
        desc=request.POST['desc'],

    )
    newcour.save()
    return redirect('/')

def disply(request, _id):
        course = courses.objects.get(id=_id)
        context = {
            'course': course

        }
        return render(request, 'remove.html', context)

def delete(request,_id):
    course = courses.objects.get(id=_id)
    course.delete()
    return redirect('/')