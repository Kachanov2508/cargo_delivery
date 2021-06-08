from django import template
from menu.models import Menu


register = template.Library()


@register.inclusion_tag('menu/menu.html')
def show_menu(user):
    context = Menu.objects.all()
    return {'context': context, 'user': user}
