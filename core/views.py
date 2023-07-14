from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Vacancy, Company
from django.contrib.auth.models import User
from .forms import VacancyForm, CompanyForm


# Create your views here.
def homepage(request):
    return render(request=request, template_name='index.html')

def about_us(request):
    return render(request, 'about_us.html')

def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {"vacancies": vacancy_list}
    return render(request, 'vacancy/vacancies.html', context)

def reg_view(request):
    if request.method == "POST":
        user = User(
            username=request.POST["username"]
        )
        user.save()
        user.set_password(request.POST["password"])
        user.save()
        return HttpResponse('Регистрация завершена')
    return render(
        request,
        "auth/registration.html"
    )

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

def add_vacancy(request):
    if request.method == "POST":
        new_vac = Vacancy(
            title=request.POST["form-title"],
            salary=int(request.POST["form-salary"]),
            description=request.POST["form-descr"],
            email=request.POST["form-email"],
            contacts=request.POST["form-cont"]
        )
        new_vac.save()
        return redirect(f'/vacancy/{new_vac.id}/')
    return render(request, 'vacancy/add_vacancy.html')

def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST["title"]
        vacancy.salary = int(request.POST["salary"])
        vacancy.description = request.POST["description"]
        vacancy.email = request.POST["email"]
        vacancy.contacts = request.POST["contacts"]
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')
    return render(
        request, 'vacancy/vacancy_edit_form.html',
        {"vacancy": vacancy}
    )

def vacancy_add_via_django_form(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm()
    return render(
        request,
        'vacancy/vacancy_django_forms.html',
        {'vacancy_form': vacancy_form}
    )

def vacancy_edit_via_form(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    if request.method == "GET":
        form = VacancyForm(instance=vacancy_object)
        return render(request, 'vacancy/vacancy_edit_dj_forms.html',
                      {'form': form})

    elif request.method == "POST":
        form = VacancyForm(data=request.POST, instance=vacancy_object)
        if form.is_valid():
            object = form.save()
            return redirect(vacancy_info, id=object.id)
        else:
            return HttpResponse('Форма не валидна')

def company_list(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'company/companies.html', context)

def company_info(request, id):
    company = Company.objects.get(id=id)
    employee = company.employee.all()
    return render(
        request,
        'company/company-info.html',
        {
            'company': company,
            'employee': employee
        }
    )

def company_add_via_django_forms(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save()
            return redirect(f'/company-info/{new_company.id}/')
    company_form = CompanyForm()
    return render(
        request,
        'company/company_django_forms.html',
        {'company_form': company_form}
    )

def company_edit_via_django(request, id):
    company_object = Company.objects.get(id=id)
    if request.method == "GET":
        form = CompanyForm(instance=company_object)
        return render(
            request,
            'company/company_edit.html',
            {'form': form}
        )
    elif request.method == "POST":
        form = CompanyForm(data=request.POST, instance=company_object)
        if form.is_valid():
            obj = form.save()
            return redirect(company_info, id=obj.id)
        else:
            return HttpResponse('Форма не валидна')

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Неверный логин или пароль")

    return render(request, 'auth/sign_in.html')

def sign_out(request):
    logout(request)
    return redirect(sign_in)
