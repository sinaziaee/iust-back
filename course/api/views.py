from course import models
from django.shortcuts import render, HttpResponse


def home(request):
    get = request.GET
    name = get.get('course')
    print(name)
    try:
        each = models.Course.objects.get(name=name)
        print(each)
    except Exception as e:
        print(e)
    return HttpResponse('hello')


def schedule(request):
    return HttpResponse('hello')


def lecture(request):
    return None


def assignment(request):
    return None


def final_project(request):
    return None


def course_material(request):
    return None
