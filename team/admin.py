from django.contrib import admin
from . import models


@admin.register(models.Project)
class Projects(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_time', 'end_time', 'team')
    list_filter = ('team',)
    fieldsets = (
        ('information', {
            'fields': ('name', 'description')
        }),
        ('history', {
            'fields': ('start_time', 'end_time')
        }),
        ('owner', {
            'fields': ('team',)
        })
    )


@admin.register(models.SocialMedia)
class Social(admin.ModelAdmin):
    list_display = ('name', 'team')
    list_filter = ('team',)


@admin.register(models.Skill)
class Skills(admin.ModelAdmin):
    list_display = ('name', 'score', 'team')
    list_filter = ('team',)


class ProjectsInline(admin.TabularInline):
    model = models.Project
    extra = 1


class SkillsInline(admin.TabularInline):
    model = models.Skill
    extra = 3


class SocialInline(admin.TabularInline):
    model = models.SocialMedia
    extra = 3


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status', 'create_time')
    inlines = [SocialInline, SkillsInline, ProjectsInline]
