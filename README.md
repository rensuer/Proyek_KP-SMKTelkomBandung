# Proyek_KP-SMKTelkomBandung

Requirements:
1. Python 3.11.9
2. mySQL 9.0.1
3. Django 5.1.1

Hal yang perlu diinstall sebelum menjalankan proyek:
1. pip install django
2. pip install Pillow
3. pip install mysqlclient

Konfigurasi Database:
1. Ubah bagian DATABASES di settings.py, sesuaikan nama database, username, dan password (pastikan database di MySQL sudah dibuat sebelumnya)
2. Lakukan "python manage.py makemigrations" dan "python manage.py migrate"

Konfigurasi Admin:
1. Lakukan "python manage.py createsuperuser"
2. Kemudian isi username dan password yang diinginkan untuk login admin.

Setelah setiap tahap diatas sudah dilakukan maka proyek dapat dijalankan menggunakan "python manage.py runserver"

