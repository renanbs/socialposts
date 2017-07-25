from django import forms

from .models import Group


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = [
            "title",
            "url",
            "group_status",
            "admin",
            "admin_status",
            "frequency",
            "frq_scale",
        ]
