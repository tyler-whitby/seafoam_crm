from django import template
from .customer_config import *

register = template.Library()

@register.simple_tag
def customer_name():
    return customer_vars['CUSTOMER_NAME']