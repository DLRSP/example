from django import template
from django import __version__ as django_ver
from django_errors import __version__ as django_errors_ver

register = template.Library()


@register.simple_tag
def load_django_ver():
    return django_ver


@register.simple_tag
def load_django_errors_ver():
    return django_errors_ver
