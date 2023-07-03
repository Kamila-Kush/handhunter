from django.shortcuts import render, HttpResponse
from .models import Vacancy, Company
# Create your views here.
def homepage(request):
    return render(request=request, template_name='index.html')

def about_us(request):
    return render(request, 'about_us.html')

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy/vacancies.html', context)

def vacancy_info(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    candidates = vacancy_object.candidate.all()
    context = {
        'vacancy': vacancy_object,
        'candidates': candidates}
    return render(request, 'vacancy/vacancy.html', context)
def company_list(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'companies.html', context)

def search(request):
    word=request.GET["keyword"]
    vacancy_list= Vacancy.objects.filter(title__contains=word)
    context={"vacancies": vacancy_list}
    return render(request, 'vacancy/vacancies.html', context)

