from django import template
from django.urls import resolve

register = template.Library()


@register.simple_tag
def admin_filter_list(cl, spec):
    return {'choices': list(spec.choices(cl))}