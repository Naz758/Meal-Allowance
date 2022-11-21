from django import forms
from django.forms import ModelForm

from .models import Claim, Staff


class ClaimCreateForm(ModelForm):
    class Meta:
        model = Claim
        fields = "__all__"
        exclude = ("staff",)
        widgets = {
            "start_time": forms.TextInput(attrs={"type": "time"}),
            "end_time": forms.TextInput(attrs={"type": "time"}),
            "purpose": forms.Textarea(attrs={"rows": 3}),
        }
