from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url('(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_detail, name='step'),
    url('(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
