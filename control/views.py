from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .forms import ControlForm
from .models import Control
# Create your views here.


def control_list(request):
    # queryset_list = Control.objects.all().order_by("group")
    # queryset_list = Control.objects.all().filter(group__pk=1)
    queryset_list = Control.objects.all()
    # queryset_list = Control.objects.all()
    # queryset_list = Control.objects.filter(group__title__icontains="title")

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

    paginator = Paginator(queryset_list, 50)  # Show 5 contacts per page
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
