from django import template

from djsilver.models import Department, FacultyHomePageDepartments
from djsilver.config import DATABASE_NAME

register = template.Library()

class GetFacultyList(template.Node):

    def __init__(self, bits):
        self.varname = bits[2]
        department_name=bits[3:]
        dept=''
        for item in department_name:
            dept += item + " "
        self.department = dept[:-1]
        self.faculty_list = FacultyHomePageDepartments.objects.using(DATABASE_NAME).filter(departmentid__departmentname=self.department).order_by("facultyhomepageid__lastname")

    def __repr__(self):
        return "<FacultyList>"

    def render(self, context):
        try:
            context[self.varname] = self.faculty_list
        except:
            context[self.varname] = "error"
        return ''

class DoGetFaculty:
    """
    {% get_faculty as variable_name department name with spaces %}
    """

    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, parser, token):
        bits = token.contents.split()
        if len(bits) < 4:
            raise template.TemplateSyntaxError, "'%s' tag takes three arguments" % bits[0]
        if bits[1] != "as":
            raise template.TemplateSyntaxError, "First argument to '%s' tag must be 'as'" % bits[0]
        return GetFacultyList(bits)

register.tag('get_faculty', DoGetFaculty('get_faculty'))
