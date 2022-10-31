import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q
from django.views.generic import ListView, DetailView

from mainapp.models import Posts, Comment
from mainapp.forms import FollowForm
from mainapp.views import TitleContextMixin


class CategoryPopTagsContextMixin:

    def get_context_data(self, **kwargs):
        context = super(CategoryPopTagsContextMixin, self).get_context_data(**kwargs)

        # Most pop
        # Top 3 of most popular posts are rendered by random way
        context['pop_posts'] = Posts.objects.order_by('?')[:3]

        # Tags
        context['posts_tags_tuples'] = Posts.objects.values_list('tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5')
        posts_tags = []
        for el in context['posts_tags_tuples']:
            for tag in el:
                if tag:
                    posts_tags.append(tag)
        context['posts_tags'] = posts_tags
        posts_tags = random.sample(list(set(posts_tags)), 7)
        context['posts_tags'] = posts_tags

        # Category
        context['posts_categories'] = Posts.objects.values('category').order_by('category').annotate(
            the_count=Count('category'))

        # All posts
        context['post_quantity'] = Posts.objects.all()

        return context


class PaginationContextMixin:

    def get_context_data(self, **kwargs):
        context = super(PaginationContextMixin, self).get_context_data(**kwargs)
        posts_list = Posts.objects.all()
        paginator = Paginator(posts_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_posts = paginator.page(page)
        except PageNotAnInteger:
            file_posts = paginator.page(1)
        except EmptyPage:
            file_posts = paginator.page(paginator.num_pages)

        context['file_posts'] = file_posts
        return context


class BlogListView(TitleContextMixin, CategoryPopTagsContextMixin, PaginationContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'blogapp/blog-home.html'
    model = Posts

    # For renaming
    # context_object_name = "posts_list"

    paginate_by = 5


class BlogDetailView(TitleContextMixin, CategoryPopTagsContextMixin, DetailView):
    title = 'Блог | Пост - YogaHanna'
    template_name = 'blogapp/blog-single.html'
    model = Posts


class BlogCategoryListView(TitleContextMixin, CategoryPopTagsContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'blogapp/blog-home.html'
    model = Posts

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        context['posts_list'] = Posts.objects.filter(category=self.kwargs['pk'])
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form

        return context


class BlogTagListView(TitleContextMixin, CategoryPopTagsContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'blogapp/blog-home.html'
    model = Posts

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )

        tag = self.kwargs['pk']
        context['posts_list'] = Posts.objects.filter(
            Q(tag_1=tag) | Q(tag_2=tag) | Q(tag_3=tag) | Q(tag_4=tag) | Q(tag_5=tag)
        )
        input_follow_form = FollowForm()
        context['input_follow_form'] = input_follow_form

        return context


class BlogNameListView(TitleContextMixin, CategoryPopTagsContextMixin, ListView):
    title = 'Блог - YogaHanna'
    template_name = 'blogapp/blog-home.html'
    model = Posts

    def get_queryset(self):
        title = self.request.GET.get('posts_title')
        posts_list = Posts.objects.filter(Q(headers__icontains=title) | Q(short_description__icontains=title))
        return posts_list
