from django import template
from django.shortcuts import redirect

from order_form.forms import OrderForm

register = template.Library()


@register.inclusion_tag('order_form/order_form.html')
def show_order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
    return {'context': 'show order form', 'form': form}
