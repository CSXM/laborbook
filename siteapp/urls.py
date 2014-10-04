from django.conf.urls import patterns, url

from siteapp import views

# Refer to views.py about test_pattern_list
test_pattern_list = []

for test_view in views.getTestViews():
        test_pattern_list.append(url(test_view['url_string'], getattr(views, test_view['name']), name=test_view['name']))

urlpatterns = patterns('',
    url(r'^$', views.site_index, name='index'),
    * test_pattern_list # <- add the test pattern list as args with *
)