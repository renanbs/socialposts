from django import forms

from .models import Group


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = [
            "title",
            "url",
            "admin",
            "status",
            "frequency",
            "frq_scale",
            "obs",
        ]
