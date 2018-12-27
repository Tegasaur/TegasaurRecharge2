from django import template

register=template.Library()

@register.filter
def b(things,value):
    return things.filter(price=value)

register.filter('sams2',b)
