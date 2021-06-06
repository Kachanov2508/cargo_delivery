from django import template
from header.models import Header

register = template.Library()


@register.inclusion_tag('header/header.html')
def show_header():
    context = Header.objects.all()
    return {'context': context}
