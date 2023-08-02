from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import ArticleNew
from .forms import ArticleForm

class ArticleView(View):
    def get(self, request):
        article = ArticleNew.objects.all()
        return render(request, 'article/list.html', {'article': article})

class ArticleCreateView(CreateView):
    template_name ='article/create.html'
    model = ArticleNew
    fields = '__all__'
    success_url = reverse_lazy('list')


class ArticleDetailView(View):
    template = "article/detail.html"
    def get_context(self, **kwargs):
        pk = kwargs["pk"]
        article_object = ArticleNew.objects.get(pk=pk)
        form = ArticleForm(instance=article_object)
        context = {}
        context["form"] = form
        return context

    def counter(self):
        return self.views_count +=1


class ArticleUpdate(UpdateView):
    model = ArticleNew
    fields = [f.name for f in ArticleNew._meta.get_fields() if f.name not in ['id', 'user']]
    template_name = 'article/update.html'
    success_url = reverse_lazy('article-list')