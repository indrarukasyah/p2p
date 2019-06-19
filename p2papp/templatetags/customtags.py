from django import template
from django.template.loader import render_to_string
from django.urls import resolve

register = template.Library()


@register.simple_tag
def admin_filter_list(cl, spec):
    choices = {'choices':list(spec.choices(cl))}
    return render_to_string('tags_html/admin_filter_list.html',choices)

@register.simple_tag
def dir_context(context):
    print(dir(context))
    return context

@register.simple_tag
def admin_lists_display(context):
    data = {'display': context.list_display, 'queryset': context.queryset}
    return render_to_string('tags_html/admin_lists_display.html', data)

@register.simple_tag
def show_list_name(query,name):
    x = str(name)
    print(query)
    return True