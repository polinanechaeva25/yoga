from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blogapp.views import BlogListView, BlogDetailView, BlogCategoryListView, BlogTagListView, BlogNameListView

app_name = 'blogapp'

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('name/', BlogNameListView.as_view(), name='name'),
    path('<int:pk>/', BlogDetailView.as_view(), name='single'),
    path('category/<str:pk>/', BlogCategoryListView.as_view(), name='category'),
    path('tag/<str:pk>/', BlogTagListView.as_view(), name='tag'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
