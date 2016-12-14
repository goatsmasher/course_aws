from django.shortcuts import render, redirect
from .models import Course
def index(request):
    context = {
        'all_courses' : Course.objects.all(),
    }
    print context
    return render(request, 'main_app/index.html', context)

def remove(request, id):
    del_course = Course.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'main_app/del_course.html', {'course' : del_course})
    del_course.delete()
    return redirect('/')

def create(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')