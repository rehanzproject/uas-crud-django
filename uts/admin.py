from django.contrib import admin
from .models import Buku ,Jenis , Waktu

class pinjamBuku(admin.ModelAdmin):
    list_display = ['nama_buku','penerbit','stok','jumlah_halaman','gbr_buku','jenis_buku']
    search_fields= ['nama_buku','penerbit']
    list_filter = ['jenis_buku',]
    list_per_page= 5

admin.site.register(Buku, pinjamBuku)
admin.site.register(Waktu)
admin.site.register(Jenis)
# Register your models here.
