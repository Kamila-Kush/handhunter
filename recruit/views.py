from django.shortcuts import render, HttpResponse, redirect
from .models import Recruit

def recruit(request):
    recruit = Recruit.objects.all()
    return render(
        request,
        'recruit_list.html',
        {recruit: "recruit"}
    )