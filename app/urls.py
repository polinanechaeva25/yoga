from django.contrib import admin
from django.urls import path
from django.conf import settings
# from django.conf.urls import include
from django.conf.urls.static import static

from mainapp.views import MainListView, ContactListView, AboutListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('about/', AboutListView.as_view(), name='about'),
]
