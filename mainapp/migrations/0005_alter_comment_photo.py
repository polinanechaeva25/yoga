# Generated by Django 4.1.2 on 2022-10-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_comment_course_comment_is_checked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, default='/unknowing/default.png', upload_to='comment_photo'),
        ),
    ]