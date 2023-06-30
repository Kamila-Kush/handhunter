from django.shortcuts import render
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
    resume_query = Resume.objects.all()
    return render(
        request, 'resume/resume_list.html',
        {'resume: resume_query'}
    )

def resume_info(request, id):
    resume_object = Resume.object.get(id=id)
    return render(
        request, 'resume/resume_detail.html',
        {'resume':resume_object}
    )

def my_resume(request):
    resume_query = Resume.objects.filter(worker=request.user.worker) # = request.user.worker.all()
    return render(
        request, 'resume/resume_list.html',
        {'resumes': resume_query}
    )