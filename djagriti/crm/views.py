from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from cms.models import *
from cms.forms import *
from crm.forms import *
from crm.models import Price as PriceView
from telegram import *
from django.contrib.auth.models import User


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


@login_required
def dashboard(request):
    order = Order.objects.all()
    return render(request, 'crm/dashboard.html', {'order': order, 'title': "Панель управления"})


def show_post(request, post_slug):
    form = OrderForm()
    post = get_object_or_404(CmsTeachers, slug=post_slug)
    return render(request, 'crm/teacher_about.html', {'post': post, 'form': form, 'title': 'О тренерах'})


@login_required
def delete_order(request, id_order):
    order = Order.objects.get(pk=id_order)
    order.delete()
    return redirect('dashboard')


@login_required
def update_order(request, id_order):
    order = Order.objects.get(pk=id_order)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'crm/update_order.html', {'order': order, 'form': form})


@login_required
def delete_teacher(request, id_teacher):
    teacher = CmsTeachers.objects.get(pk=id_teacher)
    teacher.delete()
    return redirect('admin_teachers')


@login_required
def update_teacher(request, id_teacher):
    teacher = CmsTeachers.objects.get(pk=id_teacher)
    form = TeacherForm(request.POST or None, request.FILES or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('admin_teachers')
    return render(request, 'crm/update_teacher.html', {'teacher': teacher, 'form': form})


@login_required
def add_teacher(request):
    form = TeacherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_teachers')
    return render(request, 'crm/add_teacher.html', {'form': form})


@login_required
def delete_price(request, id_price):
    price = Price.objects.get(pk=id_price)
    price.delete()
    return redirect('admin_price')


@login_required
def update_price(request, id_price):
    price = Price.objects.get(pk=id_price)
    form = PriceForm(request.POST or None, instance=price)
    if form.is_valid():
        form.save()
        return redirect('admin_price')
    return render(request, 'crm/update_price.html', {'price': price, 'form': form})


@login_required
def add_price(request):
    form = PriceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_price')
    return render(request, 'crm/add_price.html', {'form': form})


@login_required
def delete_user(request, user_name):
    users = User.objects.get(username=user_name)
    users.delete()
    return redirect('show_users')




@login_required
def add_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        User.objects.create_user(**form.cleaned_data)
        return redirect('show_users')
    return render(request, 'crm/add_user.html', {'form': form})


@login_required
def admin_teachers(request):
    teacher = CmsTeachers.objects.all()
    return render(request, 'crm/admin_teachers.html', {'order': teacher, 'title': "Панель управления"})


@login_required
def admin_price(request):
    price = Price.objects.all()
    return render(request, 'crm/admin_price.html', {'order': price, 'title': "Панель управления"})


def show_users(request):
    users = User.objects.all()
    return render(request, 'crm/admin_users.html', {'users': users, 'title': "Панель управления"})
