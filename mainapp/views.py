from django.conf import settings
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from django.views import View
from django.views.generic import ListView, CreateView
from django.core.mail import send_mail, BadHeaderError


from .models import Posts, Comment
from .forms import ContactForm, MessageForm, FollowForm, CommentForm


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
        context['comment_list'] = Comment.objects.filter(is_checked=True).order_by('?')[:9]
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


class CommentView(TitleContextMixin, ListView):
    title = 'Комментарий - YogaHanna'
    template_name = 'mainapp/comment_form.html'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        comment_form = CommentForm()
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form
        context['comment_form'] = comment_form

        return context


class CommentCreateView(CreateView):

    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def post(self, request, *args, **kwargs):
        comment_form = self.form_class(self.request.POST, self.request.FILES)
        if comment_form.is_valid():

            comment_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:

            return HttpResponse('Неверно заполненная форма. Попробуйте еще раз.')