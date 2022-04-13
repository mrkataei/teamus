from django import forms
from team.models import Team


class TeamCreate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeamCreate, self).__init__(*args, **kwargs)

    class Meta:
        model = Team
        fields = ('name', 'bio', 'status', 'owner')
        widgets = {
            'owner': forms.HiddenInput()
        }


