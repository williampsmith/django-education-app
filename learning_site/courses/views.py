# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers, models

from .models import Course, Step

# NOTE: Access browsable API at http://localhost:8000/courses/api/v1/courses


# NOTE: API using generic views
class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class ListCreateStep(generics.ListCreateAPIView):
    queryset = models.Step.objects.all()
    serializer_class = serializers.StepSerializer

    # override get method of generics
    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

    # This is the method that is run right when an object is
    # being created by the view. We override it in order to disallow
    # the user from creating a step for an arbitrary course.
    def perform_create(self):
        course = get_object_or_404(
            models.Step, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)

class RetrieveUpdateDestroyStep(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Step.objects.all()
    serializer_class = serializers.StepSerializer

    # like get_query_set, but returns a single item.
    def get_object(self):
        course = models.Course.objects.filter(pk=self.kwargs.get('course_pk'))
        return get_object_or_404(
            self.get_queryset(),
            course=course,
            pk=self.kwargs.get('pk')
        )

# # NOTE: API V2
# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = models.Course.objects.all()
#     serializer = serializers.CourseSerializer
#
# class StepViewSet(viewsets.ModelViewSet):
#     queryset = models.Step.objects.all()
#     seializer = serializers.StepSerializer


# NOTE: API using non-generic view
# class ListCreateCourse(APIView):
#     def get(self, request, format=None):
#         courses = models.Course.objects.all()
#         serializer = serializers.CourseSerializer(courses, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = serializers.CourseSerializer(data=request.data)
#         # checks to make sure incoming data passes validation
#         # checks/rules provided in the model
#         serializer.is_valid(raise_exception=True)
#         # saves to database and updates serializer fields with
#         # database provided fields, such as 'created_at'.
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# Templates
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    # course = Course.objects.get(pk=pk) # without 404, conventional way
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})
