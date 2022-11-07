from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Claim, ClaimApprover, Staff


class ClaimListView(ListView):
    model = Claim


class ClaimDetailView(DetailView):
    model = Claim


class ClaimCreateView(CreateView):
    model = Claim
    fields = "__all__"
    
    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(ClaimCreateView, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        # provider = User.objects.get(pk=2)
        # initial['provider'] = provider
        initial["staff"] = self.request.user
        # etc...
        return initial


class ClaimApproverCreateView(CreateView):
    model = ClaimApprover
    fields = "__all__"


class StaffUpdateView(UpdateView):
    model = Staff
    fields = "__all__"
