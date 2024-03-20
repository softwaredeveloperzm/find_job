import django_filters
from django.shortcuts import render
from job.models import Job

class Jobfilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    state = django_filters.CharFilter(field_name='state', lookup_expr='icontains')
    job_type = django_filters.CharFilter(field_name='job_type', lookup_expr='icontains')
    industry = django_filters.CharFilter(field_name='industry', lookup_expr='icontains')
    location = django_filters.CharFilter(field_name='location', method='filter_location')  # Use custom method for filtering

    class Meta:
        model = Job
        fields = ['title', 'state', 'job_type', 'industry', 'location']  

    def filter_location(self, queryset, name, value):
        values = value.split(',')  # Split comma-separated values
        return queryset.filter(**{'{}__in'.format(name): values}) if values else queryset  # Use __in lookup for multiple values
