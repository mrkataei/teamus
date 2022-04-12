from django.db import models
from django.urls import reverse
from account.models import Member


class Team(models.Model):
    status_choice = (
        ('B', 'busy'),
        ('A', 'available')
    )
    name = models.CharField(primary_key=True, max_length=250, null=False, blank=False, unique=True)
    photo = models.ImageField(upload_to='teams-photo', null=True)
    members = models.ManyToManyField(Member)
    bio = models.TextField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=1, choices=status_choice, default='A')
    create_time = models.DateField(auto_now=True)
    owner = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE, related_name='creator')

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams_detail', args=[str(self.id)])


class Skill(models.Model):
    score_quality = (
        ('P', 'perfect'),
        ('M', 'medium'),
        ('L', 'little')
    )
    name = models.CharField(max_length=250, null=False, blank=False)
    score = models.CharField(max_length=1, choices=score_quality)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    social_media = (
        ('I', 'instagram'),
        ('L', 'linkedin'),
        ('E', 'email')
    )
    name = models.CharField(max_length=1, choices=social_media, verbose_name='social media')
    link = models.TextField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name
