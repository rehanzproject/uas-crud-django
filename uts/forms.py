from django import forms
from django.forms import ModelForm
from uts.models import Waktu , Buku

class PinjamWaktu(ModelForm):
    class Meta :
        model = Waktu
        fields='__all__'

        widgets = {
            'nama_peminjam': forms.TextInput({'class': 'form-control'}),
            'nama_buku':forms.TextInput({'class': 'form-control'}),
            'batas_waktu':forms.TextInput({'class': 'form-control'}),
            'komen':forms.TextInput({'class': 'form-control'}),
        }
class PinjamBuku(ModelForm):
    class Meta :
        model = Buku
        fields='__all__'

        widgets = {
            'nama_buku': forms.TextInput({'class': 'form-control'}),
            'penerbit':forms.TextInput({'class': 'form-control'}),
            'stok':forms.TextInput({'class': 'form-control'}),
            'jumlah_halaman':forms.TextInput({'class': 'form-control'}),
        }
