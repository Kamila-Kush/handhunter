from django.shortcuts import render, redirect, HttpResponse
from .models import Worker, Resume
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
    context = {'resume':resumes}
    return render(
        request, 'resume/resume_list.html', context)

def resume_info(request, id):
    resume_object = Resume.object.get(id=id)
    return render(
        request, 'resume/resume_detail.html',
        {'resume':resume_object}
    )

def my_resume(request):
    if request.is_authenticated:
        resume_query = Resume.objects.filter(worker=request.user.worker) # = request.user.worker.all()
        return render(
            request, 'resume/my_resume_list.html',
            {'resumes': resume_query}
        )
    else:
        return redirect('home')


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
        new_resume.save()
        return HttpResponse("Резюме сохранено")

def resume_edit(request, id):
    if request.is_authenticated:
        resume = Resume.objects.get(id=id)
        if request.method == "POST":
            resume.title = request.POST["title"]
            resume.education_degree = request.POST["education_degree"]
            resume.age = request.POST["age"]
            resume.experience_years = request.POST["experience_years"]
            resume.previous_employment = request.POST["prev_emp"]
            resume.save()
            return redirect(f'/resume/{resume.id}/')
        return render(
            request, 'resume/resume_edit.html',
            {"resume": resume}
        )
    else:
        return redirect('home')