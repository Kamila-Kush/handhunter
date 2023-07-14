"""
URL configuration for handhunter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from worker.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about_us/', about_us, name='ananas'),

    path('workers/', worker_list, name='workers'),
    path('worker/<int:id>/', worker_info),

    path('vacancies/', vacancy_list, name='vacancy_list'),
    path('vacancy/<int:id>/', vacancy_info, name='vacancy-info'),
    path('vacancy-edit/<int:id>/', vacancy_edit, name='vacancy-edit'),
    path('add-vacancy/', add_vacancy, name='add-v'),
    path('add-vacancy-df/', vacancy_add_via_django_form, name='add-vacancy-df'),
    path('vacancy-edit-df/<int:id>/', vacancy_edit_via_form, name='vacancy-edit-django'),

    path('companies/', company_list),
    path('company-info/<int:id>/', company_info, name='company-info'),
    path('add-company/', company_add_via_django_forms, name='add-company'),
    path('company-edit/<int:id>/', company_edit_via_django, name='to-edit-company'),

    path("resume-list/", resume_list),
    path("resume-info/<int:id>/", resume_info, name='resume-info'),
    path("my-resume/", my_resume, name='my-resume'),
    path('add-resume/', add_resume, name='add-resume'),
    path('add-resume-df', resume_add_via_django_form, name='add-resume-df'),
    path('resume-edit/<int:id>/', resume_edit, name='resume-edit'),
    path('resume-edit-df/<int:id>/', resume_edit_via_django_form, name='resume-edit-django'),

    path('search/', search, name='search'),

    path('registration/', reg_view, name='reg'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# http:/ ..../static/my_style.css   #/handhunter/core/static/my_style.css
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
