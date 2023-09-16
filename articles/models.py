from django.db import models
from people.models import Person

class Article(models.Model):
    name = models.CharField(verbose_name="Название", max_length = 255)
    desc = models.TextField(verbose_name="Текст")
    short_desc = models.TextField(verbose_name="Короткое описание", max_length = 255)
    date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    preview_image = models.ImageField(verbose_name="Фото в шаре", upload_to="preview_article_images/", default=False)
    full_image = models.ImageField(verbose_name="Фото новости", upload_to="full_article_images/", default=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    post = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Комментарий новости")
    author = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name="Участник")
    body = models.TextField(verbose_name="Текст комментария")
    created_on = models.DateTimeField(verbose_name="Дата написания", auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)