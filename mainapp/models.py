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
    DAILY = 'Онлайн курс "Ежедневные треннировки"'
    MORNING = 'Онлайн курс "Утренние разминки"'
    NECK = 'Онлайн курс "Красивая шея"'
    OFFLINE_GROUP = 'Очные занятия в студии'
    OFFLINE_PRIVACY = 'Персональные тренировки оффлайн'
    NOTHING = ''

    COURSE_CHOICES = (
        (DAILY, 'Ежедневные треннировки'),
        (MORNING, 'Утренние разминки'),
        (NECK, 'Красивая шея'),
        (OFFLINE_GROUP, 'Оффлайн - групповые'),
        (OFFLINE_PRIVACY, 'Оффлайн - персональные'),
        (NOTHING, 'Другое'),
    )

    LESS_MONTH = 'Занимается менее месяца'
    ONE_MONTH = 'Занимается 1 месяц'
    TWO_MONTHS = 'Занимается 2 месяца'
    THREE_MONTHS = 'Занимается 3 месяца'
    FOUR_MONTHS = 'Занимается 4 месяца'
    FIVE_MONTHS = 'Занимается 5 месяцев'
    SIX_MONTHS = 'Занимается 6 месяцев'
    MORE_HALF_YEAR = 'Занимается более полугода'
    ONE_YEAR = 'Занимается 1 год'
    TWO_YEARS = 'Занимается 2 года'
    THREE_YEARS = 'Занимается 3 года'
    MORE_THREE_YEARS = 'Занимается более трех лет'
    NOTHING = 'Ещё не занимается'

    EXPERIENCE_CHOICES = (
        (LESS_MONTH, 'Менее месяца'),
        (ONE_MONTH, '1 месяц'),
        (TWO_MONTHS, '2 месяца'),
        (THREE_MONTHS, '3 месяца'),
        (FOUR_MONTHS, '4 месяца'),
        (FIVE_MONTHS, '5 месяцев'),
        (SIX_MONTHS, '6 месяцев'),
        (MORE_HALF_YEAR, 'Более полугода'),
        (ONE_YEAR, '1 год'),
        (TWO_YEARS, '2 года'),
        (THREE_YEARS, '3 года'),
        (MORE_THREE_YEARS, 'Более 3-х лет'),
        (NOTHING, 'Не занимался/(-ась)'),
    )

    user_name = models.CharField(verbose_name='имя', max_length=128)
    email = models.EmailField(max_length=254, unique=True)
    is_checked = models.BooleanField(verbose_name='подтверждение почты', db_index=True, default=False)
    course = models.CharField(verbose_name='название курса', max_length=36, choices=COURSE_CHOICES, blank=False,
                              default=NOTHING)
    experience = models.CharField(verbose_name='продолжительность занятий', max_length=25, choices=EXPERIENCE_CHOICES,
                                  blank=False, default=NOTHING)
    comment = models.TextField(verbose_name='комментарий', max_length=254)
    photo = models.ImageField(upload_to='comment_photo', blank=True, default='/unknowing/default.png')

    def __str__(self):
        return self.user_name
