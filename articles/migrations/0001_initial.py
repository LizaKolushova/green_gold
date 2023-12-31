# Generated by Django 4.2.2 on 2023-06-22 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Текст')),
                ('short_desc', models.TextField(max_length=255, verbose_name='Короткое описание')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('preview_image', models.ImageField(default=False, upload_to='preview_image', verbose_name='Фото в шаре')),
                ('full_image', models.ImageField(default=False, upload_to='full_image', verbose_name='Фото новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Текст комментария')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.person', verbose_name='Участник')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Комментарий новости')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created_on'],
            },
        ),
    ]
