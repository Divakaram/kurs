from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from cms.models import *
from crm.forms import *
from crm.models import Price as PriceView
from telegram import *


def index(request):
    slider_list = CmsSlider.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        name = request.POST['order_name']
        phone = request.POST['order_phone']
        if form.is_valid():
            send_message(tg_name=name, tg_phone=phone)
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


def dashboard(request):
    order = Order.objects.all()
    return render(request, 'crm/dashboard.html', {'order': order, 'title': "Панель управления"})


def show_post(request, post_slug):
    form = OrderForm()
    post = get_object_or_404(CmsTeachers, slug=post_slug)
    return render(request, 'crm/teacher_about.html', {'post': post, 'form': form, 'title': 'О тренерах'})


def delete_order(request, id_order):
    order = Order.objects.get(pk=id_order)
    order.delete()
    return redirect('dashboard')


def update_order(request, id_order):
    order = Order.objects.get(pk=id_order)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'crm/update_order.html', {'order': order, 'form': form})


def show_login(request):
    return render(request, 'crm/login.html')
