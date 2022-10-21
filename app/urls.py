from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls import include
from django.conf.urls.static import static

from mainapp.views import MainListView, ContactListView, AboutListView, TrainingListView, TrainOffListView, \
    TrainOnListView, BlogListView, BlogDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('about/', AboutListView.as_view(), name='about'),
    path('training/', include('mainapp.urls', namespace='training')),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_single'),
    # path('training/', TrainingListView.as_view(), name='training'),
    # path('training/offline/', TrainOffListView.as_view(), name='offline'),
    # path('training/online/', TrainOnListView.as_view(), name='online'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
