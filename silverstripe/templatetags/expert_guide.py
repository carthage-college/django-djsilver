from django import template

from silverstripe.models import SitetreeLive,FacultyHomePageLive
from silverstripe.config import DATABASE_NAME

register = template.Library()

from django.conf import settings
import logging
logging.basicConfig(filename=settings.LOG_FILENAME,level=logging.DEBUG,)

class GetExpertGuide(template.Node):

    def __init__(self, bits):
        self.varname = bits[2]

    def __repr__(self):
        return "<ExpertGuide>"

    def render(self, context):
        request = context['request']
        tag_name = request.GET.get('tag')
        tags=[]
        for tag in SitetreeLive.metakeywords.all():
            tag.count = FacultyHomePageLive.objects.using(DATABASE_NAME).filter(id__metakeywords__icontains=tag).count()
            tags.append(tag)
        try:
            expert_list = FacultyHomePageLive.objects.using(DATABASE_NAME).filter(id__metakeywords__icontains=tag_name).order_by("lastname")
            context[self.varname] = expert_list
        except:
            context[self.varname] = ""
        context['tags'] = tags
        return ''

class DoExpertGuide:
    """
    {% get_expert_guide as variable_name %}
    we grab the tag from request.GET
    """

    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, parser, token):
        bits = token.contents.split()
        if len(bits) != 3:
            raise template.TemplateSyntaxError, "'%s' tag takes two arguments" % bits[0]
        if bits[1] != "as":
            raise template.TemplateSyntaxError, "First argument to '%s' tag must be 'as'" % bits[0]
        return GetExpertGuide(bits)

register.tag('get_expert_guide', DoExpertGuide('get_expert_guide'))