from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Worker, Resume
from .forms import ResumeEditForm
# Create your views here.
def worker_list(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'workers.html', context)

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    context = {'worker': worker_object}
    return render(request, 'worker.html', context)

def resume_list(request):
    resumes = Resume.objects.all()
    context = {'resumes': resumes}
    return render(
        request, 'resume/resume_list.html', context)

def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    return render(
        request, 'resume/resume_detail.html',
        {'resume': resume_object}
    )

def my_resume(request):
    if request.user.is_authenticated:
        resume_query = Resume.objects.filter(worker=request.user.worker) # = request.user.worker.all()
        return render(
            request, 'resume/my_resume_list.html',
            {'resumes': resume_query}
        )
    else:
        return redirect('home')

@login_required(login_url='sign-in')
def add_resume(request):
    temp = 'resume/resume_add.html'
    if request.method == "GET":
        return render(request, temp)
    elif request.method == "POST":
        new_resume = Resume()
        new_resume.worker = request.user.worker
        new_resume.title = request.POST["form-title"]
        new_resume.education_degree = request.POST["form-edu"]
        new_resume.age = request.POST["form-age"]
        new_resume.experience_years = request.POST["form-ex_y"]
        new_resume.previous_employment = request.POST["form-pr_e"]
        new_resume.profile_photo = request.POST["form-profile-photo"]
        new_resume.save()
        return HttpResponse("Резюме сохранено")

def resume_edit(request, id):
    resume = Resume.objects.get(id=id)
    if request.method == "POST":
        resume.title = request.POST["title"]
        resume.education_degree = request.POST["education_degree"]
        resume.age = request.POST["age"]
        resume.experience_years = request.POST["experience_years"]
        resume.previous_employment = request.POST["prev_emp"]
        resume.save()
        return redirect(f'/resume-info/{resume.id}/')
    return render(
        request, 'resume/resume_edit.html',
        {"resume": resume}
    )

def resume_edit_via_django_form(request, id):
    resume_object = Resume.objects.get(id=id)
    if request.method =="GET":
        form = ResumeEditForm(instance=resume_object)
        return render(request, 'resume/resume_edit_dj_forms.html',
                      {'form':form})

    elif request.method == "POST":
        form = ResumeEditForm(
            data=request.POST, instance=resume_object,
            files=request.FILES
        )
        if form.is_valid():
            object = form.save()
            return redirect(resume_info, id=object.id)
        else:
            return HttpResponse('Форма не валидна')

def resume_add_via_django_form(request):
    if request.method =="POST":
        form = ResumeEditForm(request.POST)
        if form.is_valid():
            new_resume = form.save()
            return redirect(f'/resume-info/{new_resume.id}/')
    resume_form = ResumeEditForm()
    return render(
        request,
        'resume/resume_django_forms.html',
        {'resume_form': resume_form}
    )