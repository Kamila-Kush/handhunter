from django.shortcuts import render
from .models import Worker
# Create your views here.
def worker_list(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'workers.html', context)