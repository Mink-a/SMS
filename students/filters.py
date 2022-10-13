import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='startswith')
    class Meta:
        model = Student
        fields = {'first_name','last_name'}