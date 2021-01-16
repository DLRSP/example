"""Django Views for django-errors module"""
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'index.html')


def view_bad_request(request, exception=None):
    template = loader.get_template("errors/400.html")
    return HttpResponseBadRequest(template.render(request=request))


def view_permission_denied(request, exception=None):
    template = loader.get_template("errors/403.html")
    return HttpResponseForbidden(template.render(request=request))


def view_not_found(request, exception=None):
    # Override original template - "Custom" inside the tilte
    template = loader.get_template("errors/404.html")
    return HttpResponseNotFound(template.render(request=request))


def view_internal_server_error(request):
    template = loader.get_template("errors/500.html")
    return HttpResponseServerError(template.render(request=request))
