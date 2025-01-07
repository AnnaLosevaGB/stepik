from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView


class NewsHomeView(ListView):
    model = Article


class NewsCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('news:home')


class NewsDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    # template_name = 'news/article_detail.html'


class NewsUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('news:home')
    # template_name = 'news/article_form.html'


class NewsDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news:home')
    # template_name = 'news/article_confirm_delete.html'

# def news_home(request):
#     news = Article.objects.order_by('-date')
#     return render(request, 'news/article_list.html', {'news': news})


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('news:home')
#         else:
#             error = 'Неверная форма'
#
#     form = ArticleForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#
#     return render(request, 'news/article_form.html', data)
