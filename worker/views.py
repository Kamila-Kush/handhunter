from django.shortcuts import render
from .models import Worker
# Create your views here.
def worker_list(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'workers.html', context)

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    context = {'worker': worker_object}
    return render(request, 'worker.html', context)
