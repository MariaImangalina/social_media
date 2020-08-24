from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from groups.models import Group, GroupMember

class CreateGroupView(generic.CreateView, LoginRequiredMixin):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group