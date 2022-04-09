from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^(?P<pk>)$', views.AccountDetail.as_view(), name='account-detail'),
]
