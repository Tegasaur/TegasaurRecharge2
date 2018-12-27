from django import template

register =template.Library()

@register.filter
def a(things,value):
    return things.filter(name=value)
    
@register.filter
def b(things,value):
    return things.filter(price=value)
