from django.db import models


class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    ket = models.TextField()

    def __str__(self):
        return self.nama


class Buku(models.Model):
    nama_buku = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=30)
    stok = models.BigIntegerField()
    jumlah_halaman = models.BigIntegerField()
    gbr_buku = models.CharField(max_length=150, blank=True)
    jenis_buku = models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nama_buku

class Waktu(models.Model):
    nama_peminjam = models.CharField(max_length=30)
    nama_buku = models.CharField(max_length=20)
    waktu_pinjam = models.DateTimeField(auto_now_add=True)
    batas_waktu = models.CharField(max_length=10)
    komen = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_peminjam



