from django.db import models
from django.urls import reverse

from crm.models import NaprCrm


# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name="CSS класс")

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = 'Слайды'


class CmsTeachers(models.Model):
    photo = models.ImageField(upload_to='teachers_photo/')
    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    napr = models.ForeignKey(NaprCrm, on_delete=models.PROTECT, verbose_name='Направление')
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
