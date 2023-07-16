import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_year():
    return datetime.datetime.now().strftime('%Y')

