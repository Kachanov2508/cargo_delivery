from django import template

register = template.Library()


@register.inclusion_tag('order_form/order_form.html')
def show_order_form():
    return {'context': 'show order form'}
