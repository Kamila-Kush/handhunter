from django import forms
from .models import Vacancy, Company


class VacancyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-input"}))
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'description',
            'work_experience',
            'type_of_employement',
            'skill',
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