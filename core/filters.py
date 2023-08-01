import django_filters
from .models import Vacancy


class VacancyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    work_experience__gt = django_filters.NumberFilter(field_name='work_experience', lookup_expr='gt')
    work_experience__lt = django_filters.NumberFilter(field_name='work_experience', lookup_expr='lt')
    type_of_employement = django_filters.ModelChoiceFilter(queryset='type_of_employement', lookup_expr='contains')
    # skill = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Vacancy
        fields = ['title']

class SkillFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')