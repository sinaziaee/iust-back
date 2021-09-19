from course.models import *
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status
from course.api.serializer import *


@api_view(['GET', ])
def intro(request):
    try:
        course = Course.objects.all()
        print(course)
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(f'Exception found {e}', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def home(request):
    name = request.GET.get('course')
    if name is None:
        return Response('Bad course name', status=status.HTTP_400_BAD_REQUEST)
    try:
        course = Course.objects.get(short_name=name)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('Course not found', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def schedule(request):
    name = request.GET.get('course')
    if name is None:
        return Response('Bad course name', status=status.HTTP_400_BAD_REQUEST)
    try:
        course = Course.objects.get(short_name=name)
        schedules = Schedule.objects.filter(course=course).values()
        serializer = ScheduleSerializer(data=schedules, many=True)
        return Response(serializer.initial_data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('Course not found', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def lecture(request):
    name = request.GET.get('course')
    if name is None:
        return Response('Bad course name', status=status.HTTP_400_BAD_REQUEST)
    try:
        course = Course.objects.get(short_name=name)
        lectures = Lecture.objects.filter(course=course).values()
        serializer = LectureSerializer(data=lectures, many=True)
        return Response(serializer.initial_data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('Course not found', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def assignment(request):
    name = request.GET.get('course')
    if name is None:
        return Response('Bad course name', status=status.HTTP_400_BAD_REQUEST)
    try:
        course = Course.objects.get(short_name=name)
        assignments = Assignment.objects.filter(course=course).values()
        serializer = AssignmentSerializer(data=assignments, many=True)
        return Response(serializer.initial_data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('Course not found', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def final_project(request):
    return None


@api_view(['GET', ])
def course_material(request):
    name = request.GET.get('course')
    if name is None:
        return Response('Bad course name', status=status.HTTP_400_BAD_REQUEST)
    try:
        course = Course.objects.get(short_name=name)
        course_materials = CourseMaterial.objects.filter(course=course).values()
        serializer = CourseMaterialSerializer(data=course_materials, many=True)
        return Response(serializer.initial_data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('Course not found', status=status.HTTP_400_BAD_REQUEST)
