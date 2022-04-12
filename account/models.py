from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    username = models.CharField(primary_key=True, max_length=150, unique=True)
    photo = models.ImageField(upload_to='users-photo', null=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    score_quality = (
        ('P', 'perfect'),
        ('M', 'medium'),
        ('L', 'little')
    )
    name = models.CharField(max_length=250, null=False, blank=False)
    score = models.CharField(max_length=1, choices=score_quality)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
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
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name
