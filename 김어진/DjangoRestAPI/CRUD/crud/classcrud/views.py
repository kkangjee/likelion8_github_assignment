from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

class BlogView(ListView) : #html 템플릿 : 블로그 리스트를 담은 html
    model = ClassBlog

class BlogCreate(CreateView) :  #html : form을 갖는 html
    model = ClassBlog
    field = ['title', 'body']
    success_url=reverse_lazy('list')

class BlogDetail(DetailView) : #html : 상세 페이지를 담은 html
    model=ClassBlog

class BlogUpdate(UpdateView) : #html : form을 갖는 html
    model=ClassBlog
    field = ['title', 'body']
    success_url=reverse_lazy('list')

class BlogDelete(DeleteView) : #html : 진짜 지울건지
    model = ClassBlog
    success_url=reverse_lazy('list')