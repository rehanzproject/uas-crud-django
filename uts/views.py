from django.shortcuts import render , redirect
from uts.models import Buku , Waktu
from uts.forms import PinjamBuku , PinjamWaktu
from django.contrib import messages

def register(request):
    addnama=request.POST['namaPeminjam']
    addbuku=request.POST['namaBuku']
    bataswaktu=request.POST['batasWaktu']
    komentar=request.POST['komentar']
    waktu = Waktu.objects.create(nama_peminjam=addnama,nama_buku=addbuku,batas_waktu=bataswaktu,komen=komentar)
    messages.success(request, "Peminjam telah ditambah")
    return redirect('/')

def registerBuku(request):
    addbukuu=request.POST['namaBuku']
    penerbitt=request.POST['Penerbit']
    stokj=request.POST['stok']
    jml=request.POST['jumlah']
    a=request.POST['gambar']

    
    bukuu = Buku.objects.create(nama_buku=addbukuu,penerbit=penerbitt,stok=stokj,jumlah_halaman=jml, gbr_buku=a, )
    messages.success(request, "Buku telah ditambah")
    return redirect('/')

def utama(request):
    return render (request , 'index.html')
# Create your views here.

def hapusWaktu(request , id):
    namapinjam = Waktu.objects.get(id=id)
    namapinjam.delete()
    messages.success(request, "Data telah Dihapus")
    return redirect('/')

def hapusBuku(request , id):
    namapinjam = Buku.objects.get(id=id)
    namapinjam.delete()
    messages.success(request, "Buku telah dihapus")
    return redirect('/')

def tampilBuku(request):
    bukuku = Buku.objects.all()
    konteks = {
        'bukuku': bukuku,
    }
    return render(request, 'tampil_buku.html' , konteks)

def tampilPeminjam(request):
    pinjam = Waktu.objects.all()
    konteks = {
        'pinjam': pinjam
    }

    return render(request , 'tampil_waktu.html', konteks)

def add_brg(request):
    form = PinjamWaktu()
    konteks ={
        'form':form
    }
    return render (request, 'tambah_peminjam.html', konteks )

def add_buku(request):
    form = PinjamBuku()
    ctx = {
        'form':form,
    }
    return render (request, 'tambah_buku.html', ctx )


def tentang(request):
    return render (request, 'tentang.html')

def editBukuu(request, id):
    cek = Buku.objects.get(id=id)
    ctx = {
        "cek":cek,
    }
    return render(request, 'editabel.html', ctx)

def editWaktuu(request, id):
    cek = Waktu.objects.get(id=id)
    ctx = {
        "cek":cek,
    }
    return render(request, 'edittabel.html', ctx)

def editWaktu(request ):
    id = request.POST['txtId']
    namaa = request.POST['namaPeminjam']
    bukku = request.POST['namaBuku']
   
    matkull = request.POST['batasWaktu']
    komenn = request.POST['komentar']

    Waktuu = Waktu.objects.get(id=id)
    Waktuu.nama_peminjam = namaa
    Waktuu.nama_buku = bukku
   
    Waktuu.batas_waktu = matkull
    Waktuu.komen = komenn
    Waktuu.save()
    messages.success(request, "Data telah diperbarui")

    return redirect('/')

def editBuku(request):
    id = request.POST['txtId']
    namaa = request.POST['namaPeminjam']
    bukku = request.POST['namaBuku']
    matkull = request.POST['batasWaktu']
    komenn = request.POST['komentar']

    Bukuu = Buku.objects.get(id=id)
    Bukuu.nama_buku = namaa
    Bukuu.penerbit = bukku
    Bukuu.stok = matkull
    Bukuu.jumlah_halaman = komenn
    
    Bukuu.save()
    messages.success(request, "Buku telah diperbarui")

    return redirect('/')