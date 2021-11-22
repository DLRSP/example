from django import template
from django.core.cache import cache

from example.models import MyBackground

register = template.Library()


@register.simple_tag(takes_context=True)
def load_error_img(context):
    cache_key = f"site_error_{context['error_code']}_context"
    try:
        context_cache = cache.get(cache_key)
    except Exception:
        context_cache = None

    if context_cache is None:
        try:
            custom_context = (
                MyBackground.objects.values("image__file")
                .filter(name=context["error_code"])
                .first()
            )
            context_cache = cache.set(
                cache_key, custom_context["image__file"], timeout=86400
            )
            return custom_context["image__file"]
        except Exception as err:
            print(err)

    return context_cache or ""
