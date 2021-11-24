"""Django Views for django-errors module"""
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.test.utils import override_settings
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, "index.html")


def view_bad_request(request):
    raise SuspiciousOperation()


def view_permission_denied(request):
    raise PermissionDenied()


def view_not_found(request):
    # Override original template - "Custom" inside the title
    # add your html file inside "errors/404.html"
    raise Http404()


@override_settings(TEMPLATE_ERROR_404="errors/404-js.html")
def view_not_found_with_js(request):
    raise Http404()


@override_settings(TEMPLATE_ERROR_404="errors/404-image.html")
def view_not_found_with_image(request):
    raise Http404()


@require_http_methods(["POST"])
def view_not_allowed(request):
    return HttpResponse(
        b"This text should be visible only with post request!", status=200
    )


def view_internal_server_error(request):
    raise Exception("Code 500!")
