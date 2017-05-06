from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Team

class TabularUserAdmin(admin.TabularInline):
    model = get_user_model()

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    #filter_horizontal = ('TabularUserAdmin',)
    pass