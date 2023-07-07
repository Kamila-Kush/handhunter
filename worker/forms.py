from django import forms
from .models import Resume

class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title',
                  'education_degree',
                  'age',
                  'experience_years',
                  'previous_employment'
                  ]