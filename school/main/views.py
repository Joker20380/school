from lib2to3.fixes.fix_input import context

from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import random
import csv
from .models import *
from .utils import *
from .forms import *


class Index(DataMixin, ListView):
    queryset = News.objects.order_by('-time_update')
    model = News
    template_name = 'school/index.html'
    context_object_name = 'news'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Образовательный центр")
        return dict(list(context.items()) + list(c_def.items()))

    @staticmethod
    def post_carusel():
        post_carusel = News.objects.all()[:1]
        return post_carusel

    @staticmethod
    def post_last3():
        post_last3 = News.objects.reverse()[:3]
        return post_last3

    @staticmethod
    def post_last6():
        post_last6 = News.objects.reverse()[:6]
        return post_last6

    @staticmethod
    def get_page_index():
        get_page_index = request.GET.get('page')
        return get_page_index

    @staticmethod
    def post_is_published():
        post_is_published = News.objects.all()
        return post_is_published

    @staticmethod
    def program_last6():
        program_last6 = Prog.objects.all()
        return program_last6


class ShowNews(DataMixin, DetailView):
    paginate_by = 1
    model = News
    template_name = 'school/news.html'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['news'])
        return dict(list(context.items()) + list(c_def.items()))

    @staticmethod
    def post_last3():
        post_last3 = News.objects.reverse()[:3]
        return post_last3

    @staticmethod
    def post_last6():
        post_last6 = News.objects.reverse()[:6]
        return post_last6


class ShowDoc(DataMixin, DetailView):
    paginate_by = 1
    model = Documents
    template_name = 'school/doc-view.html'
    slug_url_kwarg = 'doc_slug'
    context_object_name = 'doc'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['doc'])
        return dict(list(context.items()) + list(c_def.items()))

    @staticmethod
    def post_last3():
        post_last3 = News.objects.reverse()[:3]
        return post_last3

    @staticmethod
    def post_last6():
        post_last6 = News.objects.reverse()[:6]
        return post_last6


class About(DataMixin, ListView):
    queryset = News.objects.order_by('-time_update')
    model = News
    template_name = 'school/about.html'
    context_object_name = 'news'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О нас")
        return dict(list(context.items()) + list(c_def.items()))


    @staticmethod
    def docs_all_about():
        docs_all = Documents.objects.filter(section__id=1).order_by('-time_update')
        return  docs_all

    @staticmethod
    def post_last3():
        post_last3 = News.objects.reverse()[:3]
        return post_last3

    @staticmethod
    def post_last6():
        post_last6 = News.objects.reverse()[:6]
        return post_last6

    @staticmethod
    def get_page_index():
        get_page_index = request.GET.get('page')
        return get_page_index

    @staticmethod
    def post_is_published():
        post_is_published = News.objects.all()
        return post_is_published

    @staticmethod
    def program_last6():
        program_last6 = Prog.objects.all()
        return program_last6

def add_user_to_prog(request, prog_id):
    prog = get_object_or_404(Prog, id=prog_id)
    prog.registration.add(request.user)
    return redirect('personal_area')



def personal_area(request):
    if request.method == 'POST':
        form = PersonalAreaForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('personal_area'))
    else:
        form = PersonalAreaForm(instance=request.user)
    context = {'form': form}
    return render(request, 'school/personal-area.html', context)

