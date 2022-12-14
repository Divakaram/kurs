# Generated by Django 4.0.6 on 2022-07-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NaprCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('napr_name', models.CharField(max_length=100, verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_name', models.CharField(max_length=25, verbose_name='Название')),
                ('price_value', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateTimeField(auto_now=True)),
                ('order_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('order_phone', models.CharField(max_length=18, verbose_name='Телефон')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('order_napr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.naprcrm', verbose_name='Направление')),
                ('order_price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.price', verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
