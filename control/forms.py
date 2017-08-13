from django import forms

from .models import Control


class ControlForm(forms.ModelForm):
    published = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Control
        fields = [
            "group",
            "post",
            "published",
        ]
