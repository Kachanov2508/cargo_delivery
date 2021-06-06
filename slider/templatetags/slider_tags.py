from django import template
from slider.models import Slider

register = template.Library()


@register.inclusion_tag('slider/slider.html')
def show_slider():
    context = Slider.objects.all()
    return {'context': context}
