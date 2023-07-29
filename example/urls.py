"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django_errors import views as errors_views

from .views import (
    index,
    view_bad_request,
    view_internal_server_error,
    view_not_allowed,
    view_not_found,
    view_not_found_with_image,
    view_not_found_with_js,
    view_permission_denied,
)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("", index, name="index"),
    re_path(r"", include("django_errors.urls")),
    path("bad_request/", view_bad_request, name="bad_request"),
    path("permission_denied/", view_permission_denied, name="permission_denied"),
    path("not_found/", view_not_found, name="not_found"),
    path("not_found_with_js/", view_not_found_with_js, name="not_found_with_js"),
    path(
        "not_found_with_image/", view_not_found_with_image, name="not_found_with_image"
    ),
    path("not_allowed/", view_not_allowed, name="not_allowed"),
    path("internal_error/", view_internal_server_error, name="internal_server_error"),
    path("i18n/", include("django.conf.urls.i18n")),
    re_path(r"^filer/", include("filer.urls")),
]

# @># Server Static Files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# @># Server Media Files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = errors_views.custom_400
""" Handle 400 error """

handler403 = errors_views.custom_403
""" Handle 403 error """

handler404 = errors_views.custom_404
""" Handle 404 error """

handler500 = errors_views.custom_500
""" Handle 500 error """
