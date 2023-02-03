"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
from uts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', utama),
    path('Tbuku/' ,tampilBuku),
    path('Tpeminjam/' ,tampilPeminjam),
    path('tambah/', add_brg),
    path('tambahbuku/', add_buku),
    path('registerbuku/', registerBuku),
    path('register/', register),
    path('Tpeminjam/editTbl/<id>' , editWaktuu),
    path('Tpeminjam/delTbl/<id>' , hapusWaktu),
    path('editPeminjam/' , editWaktu),
    path('Tbuku/delTbl/<id>', hapusBuku),
    path('Tbuku/editTbl/<id>' , editBukuu),
    path('editBuku/', editBuku),
    path('tentang/' ,tentang),
    
]
