import random

from django.conf import settings
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
# from django.shortcuts import render
from mainapp.forms import ContactForm, MessageForm, FollowForm
from mainapp.models import Posts, Comment
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm, MessageForm, FollowForm


class TitleContextMixin:

    def get_title(self):
        return getattr(self, 'title', '')

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form
        return context


class CategoryPopTagsContextMixin:

    def get_context_data(self, **kwargs):
        context = super(CategoryPopTagsContextMixin, self).get_context_data(**kwargs)

        # Most pop
        # Top 3 of most popular posts are rendered by random way
        context['pop_posts'] = Posts.objects.order_by('?')[:3]

        # Tags
        context['posts_tags_tuples'] = Posts.objects.values_list('tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5')
        posts_tags = []
        for el in context['posts_tags_tuples']:
            for tag in el:
                if tag:
                    posts_tags.append(tag)
        context['posts_tags'] = posts_tags
        posts_tags = random.sample(list(set(posts_tags)), 7)
        context['posts_tags'] = posts_tags

        # Category
        context['posts_categories'] = Posts.objects.values('category').order_by('category').annotate(
            the_count=Count('category'))

        # All posts
        context['post_quantity'] = Posts.objects.all()

        return context


class PaginationContextMixin:

    def get_context_data(self, **kwargs):
        context = super(PaginationContextMixin, self).get_context_data(**kwargs)
        posts_list = Posts.objects.all()
        paginator = Paginator(posts_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_posts = paginator.page(page)
        except PageNotAnInteger:
            file_posts = paginator.page(1)
        except EmptyPage:
            file_posts = paginator.page(paginator.num_pages)

        context['file_posts'] = file_posts
        return context


class MainListView(TitleContextMixin, ListView):
    title = 'YogaHanna'
    template_name = 'mainapp/index.html'
    model = Posts

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        context['object_list'] = context['object_list'][:3]
        context['comment_list'] = Comment.objects.all()[:9]
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form

        return context


class ContactListView(TitleContextMixin, ListView):
    title = 'Контакты - YogaHanna'
    template_name = 'mainapp/contact.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        input_form = ContactForm()
        mess_form = MessageForm()
        context['input_form'] = input_form
        context['mess_form'] = mess_form
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form
        return context


class AboutListView(TitleContextMixin, ListView):
    title = 'Обо мне - YogaHanna'
    template_name = 'mainapp/about.html'
    model = User


class TrainingListView(TitleContextMixin, ListView):
    title = 'Тренировки - YogaHanna'
    template_name = 'mainapp/training.html'
    model = User


class TrainOffListView(TitleContextMixin, ListView):
    title = 'Оффлайн занятия - YogaHanna'
    template_name = 'mainapp/offline.html'
    model = User


class TrainOnListView(TitleContextMixin, ListView):
    title = 'Онлайн занятия - YogaHanna'
    template_name = 'mainapp/online.html'
    model = User


class TrainOnFirstListView(TitleContextMixin, ListView):
    title = 'Каждый день | Курс - YogaHanna'
    template_name = 'mainapp/daily_course.html'
    model = User


class TrainOnSecListView(TitleContextMixin, ListView):
    title = 'Зарядка | Курс - YogaHanna'
    template_name = 'mainapp/morning.html'
    model = User


class TrainOnThirdListView(TitleContextMixin, ListView):
    title = 'Красивая шея | Курс - YogaHanna'
    template_name = 'mainapp/neck.html'
    model = User


class BlogListView(TitleContextMixin, CategoryPopTagsContextMixin, PaginationContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'mainapp/blog-home.html'
    model = Posts

    # For renaming
    # context_object_name = "posts_list"

    paginate_by = 5


class BlogDetailView(TitleContextMixin, CategoryPopTagsContextMixin, DetailView):
    title = 'Блог | Пост - YogaHanna'
    template_name = 'mainapp/blog-single.html'
    model = Posts


class BlogCategoryListView(TitleContextMixin, CategoryPopTagsContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'mainapp/blog-home.html'
    model = Posts

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        context['posts_list'] = Posts.objects.filter(category=self.kwargs['pk'])
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form

        return context


class BlogTagListView(TitleContextMixin, CategoryPopTagsContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'mainapp/blog-home.html'
    model = Posts

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )

        tag = self.kwargs['pk']
        context['posts_list'] = Posts.objects.filter(
            Q(tag_1=tag) | Q(tag_2=tag) | Q(tag_3=tag) | Q(tag_4=tag) | Q(tag_5=tag)
        )
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form

        return context


class BlogNameListView(TitleContextMixin, CategoryPopTagsContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'mainapp/blog-home.html'
    model = Posts

    def get_queryset(self):
        title = self.request.GET.get('posts_title')
        # posts_list = Posts.objects.filter(Q(headers__icontains=title) | Q(short_description__icontains=title))
        posts_list = Posts.objects.filter(headers__icontains=title)
        return posts_list


class EmailListView(View):

    form_class1 = ContactForm
    form_class2 = MessageForm

    def get(self, request):
        return redirect("contact")

    def post(self, request):

        cont_form = self.form_class1(request.POST)
        mess_form = self.form_class2(request.POST)
        if cont_form.is_valid() and mess_form.is_valid():
            body = {
                'name': cont_form.cleaned_data['name'],
                'subject': cont_form.cleaned_data['subject'],
                'email': cont_form.cleaned_data['email_address'],
                'message': mess_form.cleaned_data['message'],
            }
            subject = f"Клиентский запрос, ТЕМА: {body['subject']}"
            message = f'Email: {body["email"]}\nName:{body["name"]}\nMessage:\n{body["message"]}.'

            try:
                print(f'sending message: {message}')
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['polina2000_21@mail.ru'])
            except BadHeaderError:
                print('Nope')
                return HttpResponse('Invalid header found.')
            return redirect("contact")


class EmailFollowView(View):

    form_class = FollowForm

    def get(self, request):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def post(self, request):

        follow_form = self.form_class(request.POST)
        if follow_form.is_valid():
            body = {
                'email': follow_form.cleaned_data['email_address'],
            }
            subject = f"Запрос на подписку от: {body['email']}"
            message = f'Email: {body["email"]}.'

            try:
                print(f'sending message: {message}')
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['polina2000_21@mail.ru'])
            except BadHeaderError:
                print('Nope')
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))