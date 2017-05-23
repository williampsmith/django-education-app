from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url(r'html/(?P<course_pk>\d+)/(?P<step_pk>\d+)$',
        views.step_detail,
        name='step'),
    url(r'html/(?P<pk>\d+)/$',
        views.course_detail,
        name='detail'),
    url(r'api/v1/courses/$',
        views.ListCreateCourse.as_view(),
        name='api_course_list'),
    url(r'api/v1/courses/(?P<pk>[0-9]+)/$',
        views.RetrieveUpdateDestroyCourse.as_view(),
        name='api_course_detail'),
    url(r'^api/v1/courses/(?P<course_pk>[0-9]+)/steps/$',
        views.ListCreateStep.as_view(),
        name='api_step_list'),
    url(r'^api/v1/courses/(?P<course_pk>[0-9]+)/steps/(?P<pk>[0-9]+)/$',
        views.RetrieveUpdateDestroyStep.as_view(),
        name='api_step_detail'),
]
