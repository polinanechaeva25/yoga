# Generated by Django 4.1.2 on 2022-10-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_comment_remove_posts_extra_img_5'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.CharField(choices=[('Онлайн курс "Ежедневные треннировки"', 'Ежедневные треннировки'), ('Онлайн курс "Утренние разминки"', 'Утренние разминки'), ('Онлайн курс "Красивая шея"', 'Красивая шея'), ('Очные занятия в студии', 'Оффлайн - групповые'), ('Персональные тренировки оффлайн', 'Оффлайн - персональные'), ('', 'Другое')], default='Ещё не занимается', max_length=36, verbose_name='название курса'),
        ),
        migrations.AddField(
            model_name='comment',
            name='is_checked',
            field=models.BooleanField(db_index=True, default=False, verbose_name='подтверждение почты'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='experience',
            field=models.CharField(choices=[('Занимается менее месяца', 'Менее месяца'), ('Занимается 1 месяц', '1 месяц'), ('Занимается 2 месяца', '2 месяца'), ('Занимается 3 месяца', '3 месяца'), ('Занимается 4 месяца', '4 месяца'), ('Занимается 5 месяцев', '5 месяцев'), ('Занимается 6 месяцев', '6 месяцев'), ('Занимается более полугода', 'Более полугода'), ('Занимается 1 год', '1 год'), ('Занимается 2 года', '2 года'), ('Занимается 3 года', '3 года'), ('Занимается более трех лет', 'Более 3-х лет'), ('Ещё не занимается', 'Не занимался/(-ась)')], default='Ещё не занимается', max_length=25, verbose_name='продолжительность занятий'),
        ),
    ]
