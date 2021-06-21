from django import template
from menu.models import Menu, Footer


register = template.Library()


@register.inclusion_tag('menu/menu.html')
def show_menu(user):
    context = Menu.objects.all()
    return {'context': context, 'user': user}


@register.inclusion_tag('footer/footer.html')
def show_footer():
    context = Footer.objects.all()
    return {'company': '© 2021  ГК «ОМЕГА»', 'context': context}
