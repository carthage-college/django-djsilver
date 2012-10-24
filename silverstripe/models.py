# -*- coding: utf-8 -*-
from django.db import models
import tagging

class SitetreeLive(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    classname = models.CharField(max_length=60, db_column='ClassName', blank=True)
    created = models.DateTimeField(null=True, db_column='Created', blank=True)
    lastedited = models.DateTimeField(null=True, db_column='LastEdited', blank=True)
    urlsegment = models.CharField(max_length=765, db_column='URLSegment', blank=True)
    title = models.CharField(max_length=765, db_column='Title', blank=True)
    menutitle = models.CharField(max_length=300, db_column='MenuTitle', blank=True)
    content = models.TextField(db_column='Content', blank=True)
    metatitle = models.CharField(max_length=765, db_column='MetaTitle', blank=True)
    metadescription = models.TextField(db_column='MetaDescription', blank=True)
    # 29 Aug 2011: Larry says, "metakeywords field does not work with directory. get_professor tag barfs. not certain why. see 'tagging' below, however, as a probable reason."
    #metakeywords = models.CharField(max_length=765, db_column='MetaKeywords', blank=True)
    metakeywords = models.CharField(blank=True,null=True,default='', help_text="Seperate multiple tags with a space or comma if they contain more than one word.", verbose_name='tags',max_length=765,db_column='MetaKeywords')
    extrameta = models.TextField(db_column='ExtraMeta', blank=True)
    showinmenus = models.IntegerField(db_column='ShowInMenus')
    showinsearch = models.IntegerField(db_column='ShowInSearch')
    homepagefordomain = models.CharField(max_length=300, db_column='HomepageForDomain', blank=True)
    providecomments = models.IntegerField(db_column='ProvideComments')
    sort = models.IntegerField(db_column='Sort')
    legacyurl = models.CharField(max_length=765, db_column='LegacyURL', blank=True)
    hasbrokenfile = models.IntegerField(db_column='HasBrokenFile')
    hasbrokenlink = models.IntegerField(db_column='HasBrokenLink')
    status = models.CharField(max_length=150, db_column='Status', blank=True)
    reportclass = models.CharField(max_length=150, db_column='ReportClass', blank=True)
    canviewtype = models.CharField(max_length=42, db_column='CanViewType', blank=True)
    canedittype = models.CharField(max_length=42, db_column='CanEditType', blank=True)
    todo = models.TextField(db_column='ToDo', blank=True)
    parentid = models.IntegerField(db_column='ParentID')
    version = models.IntegerField(db_column='Version')
    priority = models.CharField(max_length=15, db_column='Priority', blank=True)
    expirydate = models.DateTimeField(null=True, db_column='ExpiryDate', blank=True)
    canpublishtype = models.CharField(max_length=42, db_column='CanPublishType', blank=True)

    class Meta:
        db_table = u'SiteTree_Live'

    def __unicode__(self):
        return self.urlsegment

tagging.register(SitetreeLive, tag_descriptor_attr="metakeywords")

class Department(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    classname = models.CharField(max_length=30, db_column='ClassName', blank=True)
    created = models.DateTimeField(null=True, db_column='Created', blank=True)
    lastedited = models.DateTimeField(null=True, db_column='LastEdited', blank=True)
    departmentname = models.TextField(db_column='DepartmentName', blank=True)

    class Meta:
        db_table = u'Department'

    def __unicode__(self):
        return self.departmentname

class File(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    classname = models.CharField(max_length=36, db_column='ClassName', blank=True)
    created = models.DateTimeField(null=True, db_column='Created', blank=True)
    lastedited = models.DateTimeField(null=True, db_column='LastEdited', blank=True)
    name = models.CharField(max_length=765, db_column='Name', blank=True)
    title = models.CharField(max_length=765, db_column='Title', blank=True)
    filename = models.CharField(max_length=765, db_column='Filename', blank=True)
    content = models.TextField(db_column='Content', blank=True)
    sort = models.IntegerField(db_column='Sort')
    parentid = models.IntegerField(db_column='ParentID')
    ownerid = models.IntegerField(db_column='OwnerID')

    class Meta:
        db_table = u'File'

    def __unicode__(self):
        return self.filename

class FacultyHomePageLive(models.Model):
    id = models.ForeignKey(SitetreeLive, primary_key=True, db_column='ID')
    firstname = models.TextField(db_column='FirstName', blank=True)
    lastname = models.TextField(db_column='LastName', blank=True)
    title = models.TextField(db_column='Title', blank=True)
    email = models.TextField(db_column='Email', blank=True)
    officephone = models.TextField(db_column='OfficePhone', blank=True)
    officehours = models.TextField(db_column='OfficeHours', blank=True)
    education = models.TextField(db_column='Education', blank=True)
    biography = models.TextField(db_column='Biography', blank=True)
    researchinterests = models.TextField(db_column='ResearchInterests', blank=True)
    largephotoid = models.IntegerField(db_column='LargePhotoID')
    smallphotoid = models.ForeignKey(File, db_column='SmallPhotoID')
    officelocation = models.TextField(db_column='OfficeLocation', blank=True)
    homepage = models.TextField(db_column='HomePage', blank=True)
    carthageid = models.TextField(db_column='CarthageID', blank=True)
    jobtitle = models.TextField(db_column='JobTitle', blank=True)
    briefbiography = models.TextField(db_column='BriefBiography', blank=True)
    extendedbiography = models.TextField(db_column='ExtendedBiography', blank=True)
    coursestaught = models.TextField(db_column='CoursesTaught', blank=True)
    featuredquote = models.TextField(db_column='FeaturedQuote', blank=True)

    class Meta:
        db_table = u'FacultyHomePage_Live'

    def __unicode__(self):
        return "%s %s" % (self.firstname,self.lastname)

class FacultyHomePageDepartments(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    facultyhomepageid = models.ForeignKey(FacultyHomePageLive, db_column='FacultyHomePageID')
    departmentid = models.ForeignKey(Department, db_column='DepartmentID')

    class Meta:
        db_table = u'FacultyHomePage_Departments'

    def __unicode__(self):
        return "%s %s" % (self.facultyhomepageid.firstname, self.facultyhomepageid.lastname)
