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
from django.template.defaulttags import url
from django.urls import path

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
    path('login/', show_login, name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
