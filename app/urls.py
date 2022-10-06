from django.contrib import admin
from django.urls import path
from django.conf import settings
# from django.conf.urls import include
from django.conf.urls.static import static

from mainapp.views import OrderListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OrderListView.as_view(), name='index'),
]
