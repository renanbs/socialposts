from django import forms
from django.conf import settings
from datetime import date, timedelta

from .models import Control

STATUS_CHOICES_INDEXED = getattr(settings, "STATUS_CHOICES_INDEXED", ())


class ControlForm(forms.ModelForm):
    published = forms.DateField(widget=forms.SelectDateWidget(), initial=date.today())

    class Meta:
        model = Control
        fields = [
            "group",
            "post",
            "published",
        ]


class FilterControl(forms.Form):

    group_status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control mb-2 mr-sm-3 mb-sm-0 ml-sm-2',
                                                                "name": "group_status"}),
                                     initial=1,
                                     label_suffix="",
                                     choices=STATUS_CHOICES_INDEXED,
                                     required=False,
                                     label="Group status")
    period_initial = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control mb-2 mr-sm-2 mb-sm-0 ml-sm-2',
                                                                   "name": "period_initial"},
                                                                   years=range(date.today().year - 10,
                                                                               date.today().year + 10)),
                                     required=False,
                                     label="Period",
                                     label_suffix="",
                                     initial=date.today()-timedelta(days=30))
    period_final = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control mb-2 mr-sm-2 mb-sm-0 ml-sm-2',
                                                                 "name": "period_final"},
                                                                 years=range(date.today().year - 10,
                                                                             date.today().year + 10)),
                                   required=False,
                                   label=" <> ",
                                   label_suffix="",
                                   initial=date.today())

