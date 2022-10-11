from django.contrib.auth.models import User
from django.views.generic import ListView
# from django.shortcuts import render


class MainListView(ListView):
    title = 'YogaHanna'
    template_name = 'mainapp/index.html'
    model = User


class ContactListView(ListView):
    title = 'Контакты - YogaHanna'
    template_name = 'mainapp/contact.html'
    model = User


class AboutListView(ListView):
    title = 'Обо мне - YogaHanna'
    template_name = 'mainapp/about.html'
    model = User