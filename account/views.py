from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import CreateTeam as TeamForm
from django.views.generic.edit import FormView


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


class CreateTeam(LoginRequiredMixin, FormView):
    login_url = '/account/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'account/create_team.html'
    form_class = TeamForm

    def post(self, request, *args, **kwargs):
        self.initial = {'owner': request.user.username}
        form = TeamForm(data=request.POST)
        if form.is_valid():
            form = TeamForm()
            pk = form.cleaned_data['name']
            self.success_url = f'/team/{pk}'
            return render(request, 'url', {'form': form})
        return render(request, 'contact-us.html', {'form': form})
    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     pk = form.cleaned_data['name']
    #     self.success_url = f'/team/{pk}'
    #     form.save()
    #     return super().form_valid(form)
