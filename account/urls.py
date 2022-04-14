from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('<pk>/', views.AccountDetail.as_view(), name='account-detail'),
    path('<pk>/create-team', views.TeamCreate.as_view(), name='create-team'),
    path('<pk>/edit-profile', views.ProfileEdit.as_view(), name='edit-profile'),
]
