from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
# from django.conf.urls import include
from django.conf.urls.static import static

from mainapp.views import MainListView, ContactListView, AboutListView, BlogListView, BlogDetailView, \
    BlogCategoryListView, BlogTagListView, BlogNameListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainListView.as_view(), name='index'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('about/', AboutListView.as_view(), name='about'),
    path('training/', include('mainapp.urls', namespace='training')),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/name/', BlogNameListView.as_view(), name='blog_name'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_single'),
    path('blog/category/<str:pk>/', BlogCategoryListView.as_view(), name='blog_category'),
    path('blog/tag/<str:pk>/', BlogTagListView.as_view(), name='blog_tag'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
