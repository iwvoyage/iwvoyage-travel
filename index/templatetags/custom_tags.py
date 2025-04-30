from django import template

register = template.Library()

@register.filter
def get_dynamic(obj, field_prefix):
    return lambda suffix: getattr(obj, f"{field_prefix}{suffix}", None)
