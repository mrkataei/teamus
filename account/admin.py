from django.contrib import admin
from . import models


@admin.register(models.Member)
class Member(admin.ModelAdmin):
    list_display = ('username', )
