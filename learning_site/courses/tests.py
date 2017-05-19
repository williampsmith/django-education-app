# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Course, Step

# Create your tests here.
class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expression",
            description="Learn to write regular expressions in Python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)

class StepModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Chillin",
            description="Learn to chill with Python"
        )

    def test_step_creation(self):
        step = Step.objects.create(
            title="Test Step 1",
            description="Test an arbitrary step",
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())

class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Learn to write tests in python."
        )
        self.course2 = Course.objects.create(
            title="New Course",
            description="A new course!"
        )
        self.step = Step.objects.create(
            title="Intrduction to Doctests",
            description="Learn to write testst in your docstring",
            course=self.course
        )

    def test_course_list_view(self):
        # self.client is a class that acts as a dummy browser in
        # order to test views. Can run get() and post() requests.
        response = self.client.get(reverse('courses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.course, response.context['courses'])
        self.assertIn(self.course2, response.context['courses'])
        self.assertTemplateUsed(response, 'courses/course_list.html')
        self.assertContains(response, self.course.title)

    def test_course_detail_view(self):
        # reverse() function takes a url name and returns the URL. This
        # is meant to avoid hard coding URL's, in case they change. We
        # can also pass in arguments that the URL might take with args/kwargs.
        response = self.client.get(reverse('courses:detail',
            kwargs={'pk': self.course.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.course, response.context['course'])
        self.assertTemplateUsed(response, 'courses/course_detail.html')

    def test_step_detail_view(self):
        response = self.client.get(reverse('courses:step', kwargs={
            'course_pk': self.course.pk,
            'step_pk': self.step.pk
        }))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.step, response.context['step'])
        self.assertTemplateUsed(response, 'courses/step_detail.html')
