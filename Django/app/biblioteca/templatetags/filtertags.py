from django import template

register = template.Library()

@register.filter(name='delete_first_word')
def delete_first_word(arg):
    return arg.split(' ', 1)[1]
