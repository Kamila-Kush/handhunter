from django import forms
from .models import ArticleNew

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleNew
        fields = '__all__'