from django import template

register = template.Library()

@register.filter(name='replace_slash')
def replace_space(value):
    return value.replace('/', ' ')