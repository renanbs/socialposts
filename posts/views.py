from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PostForm
from .models import Post
# Create your views here.


def post_list(request):
    # today = timezone.now().date()
    # queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
    queryset_list = Post.objects.all() #.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 5)  # Show 5 contacts per page
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
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, "post_list.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        # "share_string": share_string,
    }
    return render(request, "post_detail.html", context)


def post_create(request):
    print(request.user)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:list")


def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)
