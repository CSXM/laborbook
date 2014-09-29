from django.conf.urls import patterns, url

from siteapp import views

urlpatterns = patterns('',
    url(r'^$', views.site_index, name='index'),
    # url(r'^(?P<some_id>\d+)', views.test_view, name='detail'),
    # url(r'^testing2', views.testing2, name='testing2'),
    # url(r'^testing', views.testing, name='testing'),

)