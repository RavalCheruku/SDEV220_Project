from django import template

register = template.Library()

@register.filter
def modifier(stat):
    return (stat - 10) // 2
