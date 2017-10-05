from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings


def indx_view(request):

    return render(request, 'redir/index.html')


def page_not_found(request):
    return render(request, template_name='redir/404.html', context=None, content_type=None, status=404, using=None)


def permission_denied(request):
    return render(request, template_name='redir/403.html', context=None, content_type=None, status=403, using=None)


def server_error(request):
    return render(request, template_name='redir/500.html', context=None, content_type=None, status=500, using=None)


def bad_request(request):
    return render(request, template_name='redir/400.html', context=None, content_type=None, status=400, using=None)
