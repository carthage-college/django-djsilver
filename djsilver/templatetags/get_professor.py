from django import template
from django.core.cache import cache

from djsilver.config import DATABASE_NAME
from djsilver.models import  FacultyHomePageLive

register = template.Library()

class GetProf(template.Node):

    def __init__(self, bits):
        self.varname = bits[2]
        self.email=bits[3]

    def __repr__(self):
        return "<Professor>"

    def render(self, context):
        email = template.resolve_variable(self.email, context)
        key = "silverstripe_get_prof_%s" % email
        if cache.get(key):
            prof = cache.get(key)
        else:
            try:
                prof = FacultyHomePageLive.objects.using(DATABASE_NAME).get(email=email)
            except:
                prof = None
        context[self.varname] = prof
        return ''

class DoGetProf:
    """
    {% get_prof as variable_name email_address %}
    """

    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, parser, token):
        bits = token.contents.split()
        if len(bits) < 3:
            raise template.TemplateSyntaxError, "'%s' tag takes two arguments" % bits[0]
        if bits[1] != "as":
            raise template.TemplateSyntaxError, "First argument to '%s' tag must be 'as'" % bits[0]
        return GetProf(bits)

register.tag('get_prof', DoGetProf('get_prof'))
