from django.contrib import admin
from . import models


@admin.register(models.Project)
class Projects(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_time', 'end_time', 'user')
    list_filter = ('user',)
    fieldsets = (
        ('information', {
            'fields': ('name', 'bio')
        }),
        ('history', {
            'fields': ('start_time', 'end_time')
        }),
        ('owner', {
            'fields': ('user',)
        })
    )


@admin.register(models.SocialMedia)
class Social(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user',)


@admin.register(models.Skill)
class Skills(admin.ModelAdmin):
    list_display = ('name', 'score', 'user')
    list_filter = ('user',)


class ProjectsInline(admin.TabularInline):
    model = models.Project
    extra = 2


class SkillsInline(admin.TabularInline):
    model = models.Skill
    extra = 2


class SocialInline(admin.TabularInline):
    model = models.SocialMedia
    extra = 3


@admin.register(models.Member)
class Member(admin.ModelAdmin):
    list_display = ('username', )
    inlines = [SocialInline, SkillsInline, ProjectsInline]
