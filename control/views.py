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
    print(queryset_list)
    # queryset_list = Control.objects.all()
    # queryset_list = Control.objects.filter(group__title__icontains="title")

    # if request.user.is_staff or request.user.is_superuser:
    #     queryset_list = Control.objects.all()

    # query = request.GET.get("q")
    # if query:
    #     queryset_list = queryset_list.filter(
    #         Q(title__icontains=query) |
    #         Q(url__icontains=query) |
    #         Q(admin__icontains=query)
    #     ).distinct()  # avoid duplicated items
    #
    # paginator = Paginator(queryset_list, 5)  # Show 5 contacts per page
    # page_request_var = 'page'
    #
    # page = request.GET.get(page_request_var)
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset_list,
        "title": "Control",
        # "page_request_var": page_request_var,
    }
    return render(request, "control_list.html", context)

