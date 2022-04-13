from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import TeamCreate as TeamForm
from django.views.generic.edit import FormView
from team.models import Team


class AccountDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/account/login/'
    redirect_field_name = 'redirect_to'
    model = models.Member
    template_name = 'account/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(AccountDetail, self).get_context_data(**kwargs)
        context['skills'] = models.Skill.objects.filter(user=context['profile'].username)
        context['projects'] = models.Project.objects.filter(user=context['profile'].username)
        return context


class TeamCreate(LoginRequiredMixin, FormView):
    login_url = '/account/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'account/create_team.html'
    form_class = TeamForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.full_clean()
        if form.is_valid():
            pk = form.cleaned_data['name']
            self.success_url = f'/team/{pk}'
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeamForm(initial={'owner': self.request.user.username})
        return context


class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = ['bio']


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = reverse_lazy('team')
