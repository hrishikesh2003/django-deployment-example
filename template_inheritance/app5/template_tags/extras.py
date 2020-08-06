from django import template

register = template.Library()

@register.filter('cut')
#@register.filter(name='cut')-this also can be used

def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
