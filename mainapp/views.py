from django.contrib.auth.models import User
from django.views.generic import ListView
# from django.shortcuts import render


class OrderListView(ListView):
    title = 'список заказов'
    template_name = 'mainapp/index.html'
    model = User
