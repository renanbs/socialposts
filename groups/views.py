from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import GroupForm
from .models import Group
# Create your views here.


def group_list(request):
    # today = timezone.now().date()
    # queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
    queryset_list = Group.objects.all() #.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Group.objects.all()

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
        # "object_list": queryset,
        "object_list": queryset_list,
        "title": "List",
        # "page_request_var": page_request_var,
    }
    return render(request, "group_list.html", context)


