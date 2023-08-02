from django.urls import path
from .views import *

urlpatterns = [
    path('articles/', ArticleView.as_view(), name='list'),
    path('article-create/', ArticleCreateView.as_view(), name='create'),
    path('article-detail/', ArticleDetailView.as_view(), name='detail'),
    path('article-update/', ArticleUpdate.as_view(), name='update'),

]