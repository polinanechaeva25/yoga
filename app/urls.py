from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
# from django.conf.urls import include
from django.conf.urls.static import static

from mainapp.views import MainListView, ContactListView, AboutListView, EmailListView, EmailFollowView, CommentView, \
    CommentCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('about/', AboutListView.as_view(), name='about'),
    path('training/', include('mainapp.urls', namespace='training')),
    path('blog/', include('blogapp.urls', namespace='blog')),
    path('email/', EmailListView.as_view(), name='email'),
    path('email/follow/', EmailFollowView.as_view(), name='follow'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('comment/create/', CommentCreateView.as_view(), name='create'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
