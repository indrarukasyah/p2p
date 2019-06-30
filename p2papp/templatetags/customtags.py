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
    return dir(context)


@register.simple_tag
def admin_lists_display(context):

    if not '__str__' in context.list_display:
        data = {'display': context.list_display, 'queryset': context.queryset ,'LD':True}
        return render_to_string('tags_html/admin_lists_display.html', data)

    else:
        title = context.model._meta.object_name
        data = {'title':title,'display': context.list_display, 'queryset': context.queryset, 'LD': False}
        return render_to_string('tags_html/admin_lists_display.html', data)



@register.simple_tag
def show_list_name(query,name):
    if name != '__str__':
        return getattr(query,name)

    return query


@register.simple_tag
def cooltitle(name):
    return name.replace('_',' ').title()

@register.simple_tag
def coolurl(name):
    return name.id.__str__()+'/change/'

@register.simple_tag
def scale_percentage(donate,goal):
    return int(donate / goal * 100)
