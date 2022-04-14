from django.urls import path
from . import views


app_name = 'team'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<pk>/', views.TeamDetail.as_view(), name='team-detail'),
]
