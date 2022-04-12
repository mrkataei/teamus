from django.conf.urls import url
from . import views


app_name = 'team'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>[-\w]+)/$', views.TeamDetail.as_view(), name='team-detail'),
]
