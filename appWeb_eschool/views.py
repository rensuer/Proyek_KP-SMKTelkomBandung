# Create your views here.
from django.shortcuts import render
from .models import InfoEschool, RingkasanEschool, Prestasi, StrukturPengurus, Kegiatan, Testimonial, Header_Footer, Acara

def index(request):
    info = InfoEschool.objects.first()
    ringkas = RingkasanEschool.objects.first()
    prestasi = Prestasi.objects.all().order_by('-id')[:6] 
    struktur = StrukturPengurus.objects.all()
    kegiatan = Kegiatan.objects.all().order_by('id')[:4] 
    testi = Testimonial.objects.all()
    head_foot = Header_Footer.objects.first()

    # Dapatkan parameter kategori dari URL
    selected_kategori = request.GET.get('kategori', None)

    # Jika ada kategori yang dipilih, filter berdasarkan kategori tersebut
    if selected_kategori:
        acara = Acara.objects.filter(kategori_acara=selected_kategori).order_by('-id')
    else:
        # Jika tidak ada kategori dipilih, tampilkan semua acara
        acara = Acara.objects.all().order_by('-id')

    context = {
        'info': info,
        'ringkas': ringkas,
        'prestasi': prestasi,
        'struktur': struktur,
        'kegiatan': kegiatan,
        'acara': acara,
        'testi': testi,
        'head_foot': head_foot,
    }

    return render(request, 'index.html', context)
