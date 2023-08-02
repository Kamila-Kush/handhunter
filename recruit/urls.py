from django.urls import path
from .views import *



urlpatterns = [
    path('list/', recruiter_list, name='recruiter-list'),
    path('detail/<int:pk>/', recruiter_detail, name='recruiter-detail'),

    path('list-class/', RecruitView.as_view(), name='recruiter-list-class'),
    path('list-class-generic/', RecruitListView.as_view(), name='recruiter-list-class-generic'),
    path('create/', RecruiterCreateView.as_view(), name='create-recruiter'),
    path('update-g/<int:pk>/', RecruiterUpdate.as_view(), name='update-g'),
    path('update/<int:pk>/', RecruiterUpdateView2.as_view(), name='update-recruiter'),
]
