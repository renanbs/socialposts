from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import TemplateView


from datetime import date, timedelta

from .forms import ControlForm, FilterControl
from .models import Control, Group

# Create your views here.


STATUS_LIST = getattr(settings, "STATUS_LIST", ())


class ControlList(TemplateView):
    template_name = "control_list.html"

    def get_context_data(self):
        # get_context_data creates the context
        context = TemplateView.get_context_data(self)

        group_status = STATUS_LIST
        group_query_idx = 1
        period_initial = date.today() - timedelta(days=30)
        period_final = date.today()

        context.update({
            "title": "Control",
            "column": range(10),
            "group_status": group_status,
            "group_query": group_query_idx,
            "period_initial": period_initial,
            "period_final": period_final,
        })
        return context

    def get(self):
        filter_form = FilterControl()



def control_list(request):
    group_status = STATUS_LIST
    group_query_idx = 1
    period_initial = date.today()-timedelta(days=30)
    period_final = date.today()

    if request.method == "POST":
        filter_form = FilterControl(request.POST)
        if filter_form.is_valid():
            group_query_idx = int(filter_form.cleaned_data['group_status'])
            period_initial = filter_form.cleaned_data['period_initial']
            period_final = filter_form.cleaned_data['period_final']

    else:
        filter_form = FilterControl()

    if group_query_idx:
        filtered_groups = Group.objects.filter_by_status(group_status[group_query_idx])

    queryset_list = Control.objects.filter_by_group_status(group_status[group_query_idx])\
        .filter(published__range=[period_initial, period_final])

    # if request.user.is_staff or request.user.is_superuser:
    #     queryset_list = Control.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(post__content__icontains=query) |
            Q(post__title__icontains=query) |
            Q(group__title__icontains=query) |
            Q(group__admin__icontains=query) |
            Q(group__obs__icontains=query)
        ).distinct()  # avoid duplicated items

    controls_per_group = {}
    for group in filtered_groups:
        control = queryset_list.filter(group_id=group.id)
        controls_per_group[group.title] = control

    paginator = Paginator(queryset_list, 50)
    page_request_var = 'page'

    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "Control",
        "page_request_var": page_request_var,
        "controls_per_group": controls_per_group,
        "column": range(10),
        "group_status": group_status,
        "filter_form": filter_form,
    }
    return render(request, "control_list.html", context)


def control_create(request):
    print(request.user)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise Http404

    form = ControlForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "control_create.html", context)
