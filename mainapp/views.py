from django.contrib.auth.models import User
from django.views.generic import ListView
# from django.shortcuts import render


class TitleContextMixin:

    def get_title(self):
        return getattr(self, 'title', '')

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        return context


class MainListView(TitleContextMixin, ListView):
    title = 'YogaHanna'
    template_name = 'mainapp/index.html'
    model = User


class ContactListView(TitleContextMixin, ListView):
    title = 'Контакты - YogaHanna'
    template_name = 'mainapp/contact.html'
    model = User


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
