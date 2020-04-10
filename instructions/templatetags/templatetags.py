import datetime
from django import template
from num2words import num2words
from django.template.defaultfilters import stringfilter
from dAuction2.settings import UNIQUEIZER

register = template.Library()


@register.filter
def true_or_false(value):
    if value:
        return "+"
    else:
        return "-"

@register.filter
def div(value, div):
    return round((value / div) * 10, 1)/10

def div2(value, div):
    return round((value / div), 1)



@register.simple_tag
def current_time():
    return datetime.datetime.now().date()

@register.filter
@stringfilter
def format_in_3(string):
    return '.'.join([str(string)[i:i+3] for i in range(0, len(str(string)), 3)])
    # return '{:0,.2f}'.format(my_number)


@register.simple_tag
def multiply_a_and_b_and_add_bmin1(a,b):
    return (a+1)*b-1

@register.simple_tag
def multiply_a_and_b_and_add_c(a,b,c):
    return a*b+c

@register.simple_tag
def min1_and_wordify(b):
    return num2words(b-1)

@register.simple_tag
def wordify(b):
    return num2words(b)

@register.simple_tag
def plur_min1(b):
    if b>2:
        return "s"
    else:
        return ""

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def subtract_auctionid(value, arg):
    return value - (arg * UNIQUEIZER )


@register.simple_tag()
def subtract(value, arg):
    return value - arg

# @register.simple_tag
# def mod_a_and_b(a,b):
#     return divmod(a,b)

# @register.simple_tag
# def integerize(b):
#     return int(b+0.5)


