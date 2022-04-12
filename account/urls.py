from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^(?P<pk>[-\w]+)/$', views.AccountDetail.as_view(), name='account-detail'),
    url(r'^(?P<pk>[-\w]+)/create-team', views.CreateTeam.as_view(), name='create-team')
]
