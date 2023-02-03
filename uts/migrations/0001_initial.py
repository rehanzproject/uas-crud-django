# Generated by Django 4.1.3 on 2022-11-18 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Waktu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_peminjam', models.CharField(max_length=30)),
                ('nama_buku', models.CharField(max_length=20)),
                ('waktu_pinjam', models.DateTimeField(auto_now_add=True)),
                ('batas_waktu', models.CharField(max_length=10)),
                ('komen', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_buku', models.CharField(max_length=50)),
                ('penerbit', models.CharField(max_length=30)),
                ('stok', models.BigIntegerField()),
                ('jumlah_halaman', models.BigIntegerField()),
                ('gbr_buku', models.CharField(blank=True, max_length=150)),
                ('jenis_buku', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uts.jenis')),
            ],
        ),
    ]
