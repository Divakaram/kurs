from django.db import models


# Create your models here.
class NaprCrm(models.Model):
    napr_name = models.CharField(max_length=100, verbose_name='Направление')
    description = models.TextField(verbose_name="Описание", null=True)
    image = models.ImageField(upload_to="napr/", null=True)

    def __str__(self):
        return self.napr_name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Price(models.Model):
    price_name = models.CharField(max_length=25, verbose_name='Название')
    price_value = models.IntegerField(verbose_name="Цена")
    objects = models.Manager()

    def __str__(self):
        return self.price_name

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=30, verbose_name='Имя')
    order_phone = models.CharField(max_length=18, verbose_name='Телефон')
    order_napr = models.ForeignKey(NaprCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Направление')
    order_price = models.ForeignKey(Price, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Абонемент")
    date = models.DateTimeField(verbose_name="Дата и время")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
