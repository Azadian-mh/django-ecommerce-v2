from lib2to3.fixes.fix_input import context
from typing import Any
from urllib import request


from django.core.paginator import Paginator
from django.db import models
from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali
from article_module.models import Article, ArticleCategory, ArticleComment
from django.http import HttpRequest, HttpResponse


# Create your views here.


# class ArticleView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         context = {
#             'articles': articles,
#         }
#         return render(request, 'article_module/articles_page.html',context)


class ArticleListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ArticleListView, self).get_context_data(*args,**kwargs)
        context['date'] = date2jalali(self.request.user.date_joined)
        return context
    def get_queryset(self):
        query = super(ArticleListView,self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self,**kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article = Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent_id=None).order_by('-create_date').prefetch_related('articlecomment_set')
        context['comments_count'] = ArticleComment.objects.filter(article_id=article.id).count()
        return context


def article_categories_component(request : HttpRequest):
    article_main_categories = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True, parent_id=None)
    context = {
        'main_categories': article_main_categories,
    }
    return render(request, 'article_module/components/article_categories_component.html', context)



def add_article_comment(request : HttpRequest):
    if request.user.is_authenticated :
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        print(article_id, article_comment, parent_id)
        new_comment = ArticleComment(article_id=article_id, text=article_comment, parent_id=parent_id, user_id=request.user.id)
        new_comment.save()
        context = {
            'comments' : ArticleComment.objects.filter(article_id=article_id, parent_id=None).order_by('-create_date').prefetch_related('articlecomment_set'),
            'comments_count' : ArticleComment.objects.filter(article_id=article_id).count()
        }
        return render(request, 'article_module/includes/article_comments_partial.html', context)


    return HttpResponse('response')




