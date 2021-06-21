from django import template
from main_app.models import SocialBlock

register = template.Library()


@register.inclusion_tag('main_app/social_block.html')
def show_social_block():
    context = SocialBlock.objects.all()
    return {'context': context}
