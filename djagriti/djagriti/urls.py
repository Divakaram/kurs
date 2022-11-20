"""djagriti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import urls
from django.template.defaulttags import url
from django.urls import path, include

from crm import views
from crm.views import *
from djagriti import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('prepodavateli/', teachers, name='teachers'),
    path('prepodaveteli/<slug:post_slug>/', show_post, name='post'),
    path('price/', price, name='price'),
    path('dashboard/', dashboard, name='dashboard'),
    path('delete_order/<id_order>', delete_order, name='delete_order'),
    path('update_order/<id_order>', update_order, name='update_order'),
    path('delete_teacher/<id_teacher>', delete_teacher, name='delete_teacher'),
    path('update_teacher/<id_teacher>', update_teacher, name='update_teacher'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('delete_price/<id_price>', delete_price, name='delete_price'),
    path('update_price/<id_price>', update_price, name='update_price'),
    path('add_price/', add_price, name='add_price'),
    path('delete_user/<user_name>', delete_user, name='delete_user'),
    path('add_user/', add_user, name='add_user'),
    path('admin-teach/', admin_teachers, name='admin_teachers'),
    path('admin-price/', admin_price, name='admin_price'),
    path('accounts/', include('users.urls', namespace='users')),
    path('accounts/', include(urls)),
    path('admin-users/', show_users, name="show_users"),
    path('excel/', export_to_xlsx, name="excel"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
