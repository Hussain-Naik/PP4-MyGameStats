'''filter for bootstrap form validation css'''
from django import template
register = template.Library()


@register.filter(name='add_attr')
def add_attribute(field, css):
    # Accessing the already declared attributes
    attrs = field.subwidgets[0].data['attrs']
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] += f" {d}"  # Extending the class string
        else:
            key, val = d.split(':')
            attrs[key] += f'{val}'  # Extending the `key` string

    return field.as_widget(attrs=attrs)
