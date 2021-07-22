from django import template

register = template.Library()


@register.filter
def trim(value, arg):
    """Removes all whitespaces of the given string"""
    return value.strip()
