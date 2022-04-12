from django.views import generic
from . import models


class Index(generic.ListView):
    template_name = 'team/index.html'
    context_object_name = 'latest_team_list'

    def get_queryset(self):
        return models.Team.objects.order_by('create_time')


class TeamDetail(generic.DetailView):
    model = models.Team
    template_name = 'team/detail.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super(TeamDetail, self).get_context_data(**kwargs)
        context['skills'] = models.Skill.objects.filter(team=context['team'].name)
        context['projects'] = models.Project.objects.filter(team=context['team'].name)
        return context

