from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(InfoEschool)
admin.site.register(RingkasanEschool)
admin.site.register(Prestasi)
admin.site.register(StrukturPengurus)
admin.site.register(Kegiatan)
admin.site.register(Acara)
admin.site.register(Testimonial)
admin.site.register(Header_Footer)

admin.site.site_header = "Admin Website Ekschool"
admin.site.site_title = "Admin Website Ekschool"
admin.site.index_title = "Database for Website Ekschool"


