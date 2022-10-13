from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from cms.models import *
from crm.forms import *
from crm.models import Price as PriceView
from telebot.sendmessage import sendTelegram


def index(request):
    slider_list = CmsSlider.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        name = request.POST['order_name']
        phone = request.POST['order_phone']
        if form.is_valid():
            sendTelegram(tg_name=name, tg_phone=phone)
            form.save()
            return render(request, 'crm/thanks_page.html', {'slider_list': slider_list, 'form': form, 'name': name})
        else:
            return render(request, 'crm/phone_error.html', {'slider_list': slider_list, 'form': form})
    else:
        form = OrderForm()
    return render(request, 'crm/index.html', {'slider_list': slider_list, 'form': form, 'title': 'Главная'})


def teachers(requst):
    form = OrderForm()
    posts = CmsTeachers.objects.all()
    return render(requst, 'crm/teachers.html', {'form': form, 'posts': posts, 'title': 'Тренеры'})


def price(request):
    form = OrderForm()
    price_site = PriceView.objects.all()
    return render(request, 'crm/price.html', {'price_site': price_site, 'form': form, 'title': 'Цены'})


def show_post(request, post_slug):
    form = OrderForm()
    post = get_object_or_404(CmsTeachers, slug=post_slug)
    return render(request, 'crm/teacher_about.html', {'post': post, 'form': form, 'title': 'О тренерах'})
