from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls import include
from django.conf.urls.static import static

from .views import TrainingListView, TrainOffListView,\
    TrainOnListView, TrainOnFirstListView, TrainOnSecListView, TrainOnThirdListView

app_name = 'mainapp'

urlpatterns = [
    path('', TrainingListView.as_view(), name='index'),
    path('offline/', TrainOffListView.as_view(), name='offline'),
    # path('online/<int:pk>/', TrainOnListView.as_view(), name='online'),
    path('online/', TrainOnListView.as_view(), name='online'),
    path('online/1/', TrainOnFirstListView.as_view(), name='daily'),
    path('online/2/', TrainOnSecListView.as_view(), name='morning'),
    path('online/3/', TrainOnThirdListView.as_view(), name='neck'),
]