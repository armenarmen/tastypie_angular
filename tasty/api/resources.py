from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.cache import SimpleCache
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, ToOneField
from tastypie.resources import ModelResource
from registrar.models import Student, Class, StudentProject


class BareClassResource(ModelResource):
    class Meta:
        queryset = Class.objects.all()
        resource_name = "bare_class"


class StudentResource(ModelResource):
    klass = ToOneField(BareClassResource, 'klass', full=True)
    class Meta:
        queryset = Student.objects.all()
        resource_name = "student"
        allowed_methods = ['get', 'post', 'put', 'delete']  # Limit the possible REST actions
        # fields = ['title']                 # Return only these fields in the response's data
        always_return_data = True          # Whether data should be returned when a POST is made
        limit = 20                         # Number of objects per call in the list for pagination
        ordering = ['first_name']         # Default the order of the objects returned in this list
        authentication = Authentication()
        authorization = Authorization()
        cache = SimpleCache(timeout=60) # Cache this response for 60 seconds


class ClassResource(ModelResource):
    # for every Class object, tastypie will run Class.students ( or . w/e string passed in!)
    # If full is set to 'False' you will not see the info, about the student just
    # the fucking URI
    students = ToManyField(StudentResource, 'students', full=True)

    class Meta:

        # make this way faster with prefetch and/or annotate
        # http://rocketu.yetihq.com/week9/2_pm/#/2/6
        queryset = Class.objects.all()
        resource_name = "class"
        authentication = Authentication()
        authorization = Authorization()
        # tastypire takes this dict and makes it intp a filter, that would previously have to have
        # been written like poor people!
        # http://django-tastypie.readthedocs.org/en/latest/search.html?q=filtering&check_keywords=yes&area=default

        filtering = {
            'students': ALL_WITH_RELATIONS,
            'title': ['contains', 'icontains'],
            'start_date': ['gt',]
        }

# 1. Make the model in models.py!
# 2. Make the REsource, remember that tasty pie has diferent names for stuff!
# 3. Make the URL thing tooo!
# PS, make sure that all of your names are correct when you try run it on post man!
# ex Post : http://127.0.0.1:8000/api/v1/projects/
# {
#   "student": "/api/v1/student/19/",
#   "name": "BLACKMETAL"
# # }

class StudentProjectResource(ModelResource):
    # for every Class object, tastypie will run Class.students ( or . w/e string passed in!)
    # If full is set to 'False' you will not see the info, about the student just
    # the fucking URI

    #This is the thing that is fed into the json dict
    student = ToOneField(StudentResource, 'student', full=True)

    class Meta:
        queryset = StudentProject.objects.all()
        # This is the URL one
        resource_name = "projects"
        authentication = Authentication()
        authorization = Authorization()