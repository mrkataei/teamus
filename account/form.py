from django.forms import ModelForm
from team.models import Team


class CreateTeam(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__()
    #     # self.fields['photo'].required = False
    def __init__(self, *args, **kwargs):
        super(CreateTeam, self).__init__(*args, **kwargs)
        self.fields['owner'].disabled = True

    class Meta:
        model = Team
        fields = '__all__'
