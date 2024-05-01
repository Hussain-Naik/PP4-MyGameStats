'''template tags for passing variables in method'''
from django import template
register = template.Library()


@register.filter(name='grp_session_wins')
def call_method(obj, grp):
    return obj.profile.get_session_wins(grp)


@register.filter(name='grp_game_wins')
def call_method(obj, grp):
    return obj.profile.get_group_game_wins(grp)


@register.filter(name='profile_pairing')
def call_method(obj, profile):
    return obj.pairing(profile)
