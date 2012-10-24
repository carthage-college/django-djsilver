from silverstripe.models import *

import sys

try:
    dept = sys.argv[1]
except:
    print "Usage: python %s [deptartment name]" % sys.argv[0]
    sys.exit()

faculty = FacultyHomePageDepartments.objects.using('silverstripe_faculty_pages').filter(departmentid__departmentname="%s" % dept).order_by("facultyhomepageid__lastname")
for f in faculty:
    try:
        print f.facultyhomepageid.id.urlsegment
        #print f.facultyhomepageid.get_slug()
    except:
        pass

