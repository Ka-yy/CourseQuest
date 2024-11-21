from django.shortcuts import render
from .models import School, Course, Review
from .serializers import SchoolSerializer, CourseSerializer, ReviewSerializer

# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    ## Extra Functionaliy
    def get_queryset(self):
        queryset = School.objects.all()
        school_id = self.request.query_params.get('school_id', None)
        if school_id is not None:
            queryset = queryset.filter(id=school_id)
        return queryset
