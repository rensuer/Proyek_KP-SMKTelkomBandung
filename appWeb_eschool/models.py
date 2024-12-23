
# Create your models here.
from django.db import models


class InfoEschool (models.Model):
    nama = models.CharField(max_length=150)
    singkatan = models.CharField(max_length=150)
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='info/')
    form_Pendaftaran = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nama} - {self.singkatan}"

class RingkasanEschool(models.Model):
    jumlah_anggota = models.IntegerField()
    deskripsi_anggota = models.TextField()
    jumlah_prestasi = models.IntegerField()
    deskripsi_prestasi = models.TextField()
    jumlah_acara = models.IntegerField()
    deskripsi_acara = models.TextField()

    def __str__(self):
        return "Ringkasan Eschool"


class Prestasi(models.Model):
    nama_prestasi = models.CharField(max_length=255)  # Nama prestasi
    
    def __str__(self):
        return f"{self.nama_prestasi}"

class StrukturPengurus(models.Model):
    nama_pengurus = models.CharField(max_length=150)
    jabatan_pengurus = models.CharField(max_length=150)
    foto_pengurus = models.ImageField(upload_to='struktur/')

    def __str__(self):
        return f"{self.nama_pengurus} - {self.jabatan_pengurus}"

class Kegiatan(models.Model):
    nama_kegiatan = models.CharField(max_length=150)
    deskripsi_kegiatan = models.TextField()
    foto_kegiatan = models.ImageField(upload_to='kegiatan/')

    def __str__(self):
        return f"{self.nama_kegiatan}"

class Acara(models.Model):
    nama_acara = models.CharField(max_length=150)
    kategori_acara = models.CharField(max_length=150)
    url = models.URLField(max_length=250)

    def __str__(self):
        return f"{self.nama_acara} - {self.kategori_acara}"

class Testimonial(models.Model):
    nama = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='testimonial/')
    civitas = models.CharField(max_length=150)
    pesan = models.TextField()

    def __str__(self):
        return f"{self.nama} - {self.civitas}"

class Header_Footer(models.Model):
    background_web = models.ImageField(upload_to='Header/')
    info_alamat = models.TextField()
    info_kontak = models.CharField(max_length=150)
    info_jabatan = models.CharField(max_length=150)
    info_web = models.CharField(max_length=200)

    def __str__(self):
        return "Header & Footer"

