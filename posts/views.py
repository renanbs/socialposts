from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Post
# Create your views here.


def post_list(request):
    # today = timezone.now().date()
    # queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
    queryset_list = Post.objects.all() #.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

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

