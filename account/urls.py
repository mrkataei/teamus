from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^(?P<pk>[-\w]+)/$', views.AccountDetail.as_view(), name='account-detail'),
    url(r'^(?P<pk>[-\w]+)/create-team', views.TeamCreate.as_view(), name='create-team'),
    url(r'^(?P<pk>[-\w]+)/edit-profile', views.ProfileEdit.as_view(), name='edit-profile'),
]
