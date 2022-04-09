from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin


class AccountDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/account/login/'
    redirect_field_name = 'redirect_to'
    model = models.Member
    template_name = 'account/profile.html'
    context_object_name = 'profile'

