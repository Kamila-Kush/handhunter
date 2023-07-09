from django import forms
from .models import Vacancy, Company


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'description',
            'email',
            'contacts'
        ]

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'title',
            'founding_date',
            'address',
            'number_of_employees',
            'employee'
        ]