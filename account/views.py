from django.views import generic
from . import models


class AccountDetail(generic.DetailView):
    model = models.Member
    template_name = 'team/profile.html'
    context_object_name = 'profile'
