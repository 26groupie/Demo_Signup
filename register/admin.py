from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin
from neomodel import db as db

from .models import Member


class MemberAdmin(dj_admin.ModelAdmin):
    list_display = ("user",)


neo_admin.register(Member, MemberAdmin)
