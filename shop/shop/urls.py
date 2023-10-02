"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import shop_view

try:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', shop_view.index,name = 'index'),
        path('error', shop_view.error, name='error'),
        path('coaching', shop_view.coaching,name = 'coaching '),
        path('notes', shop_view.notes,name = 'notes '),
        path('download_link', shop_view.download_link,name = 'download_link '),
        path('report', shop_view.report,name = 'report '),
        path('contact', shop_view.contact,name = 'contact '),
    ]
except:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('error', shop_view.error, name='error'),]
