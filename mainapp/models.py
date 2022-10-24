from django.db import models


class Posts(models.Model):
    headers = models.CharField(verbose_name='заголовок', max_length=128, unique=True)
    short_description = models.CharField(verbose_name='короткое описание', max_length=254)
    description_1 = models.TextField(verbose_name='описание - первая половина', blank=True, max_length=2000)
    description_2 = models.TextField(verbose_name='описание - вторая половина', blank=True, max_length=2000)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации поста')
    category = models.CharField(verbose_name='Категория', max_length=64)
    is_active = models.BooleanField(verbose_name='активна', db_index=True, default=True)
    image = models.ImageField(upload_to='main_foto')
    extra_img_1 = models.ImageField(upload_to='extra_foto', blank=True)
    extra_img_2 = models.ImageField(upload_to='extra_foto', blank=True)
    extra_img_3 = models.ImageField(upload_to='extra_foto', blank=True)
    extra_img_4 = models.ImageField(upload_to='extra_foto', blank=True)
    tag_1 = models.CharField(verbose_name='тэг 1', blank=True, max_length=16)
    tag_2 = models.CharField(verbose_name='тэг 2', blank=True, max_length=16)
    tag_3 = models.CharField(verbose_name='тэг 3', blank=True, max_length=16)
    tag_4 = models.CharField(verbose_name='тэг 4', blank=True, max_length=16)
    tag_5 = models.CharField(verbose_name='тэг 5', blank=True, max_length=16)

    def __str__(self):
        return self.headers


class Comment(models.Model):
    user_name = models.CharField(verbose_name='имя', max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    experience = models.CharField(verbose_name='продолжительность занятий', max_length=16)
    comment = models.TextField(verbose_name='комментарий', max_length=254)
    photo = models.ImageField(upload_to='comment_photo')

    def __str__(self):
        return self.user_name

