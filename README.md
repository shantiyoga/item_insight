# **<font color=#FF69B4>Item Insight</font>**

**Pemrograman Berbasis Platform**<br/>
**Tugas 2: Implementasi Model-View-Template (MVT) pada Django**<br/>

**<font color="#ffc0e0">Author</font>**<br/>
Shanti Yoga Rahayu<br/>
2206082360<br/>
PBP D<br/>

Tautan menuju aplikasi Adaptable yang sudah melalui tahap deployment dapat diakses melalui

## **<font color="#F77FBE">Membuat sebuah proyek Django baru</font>**
1. Buat sebuah direktori baru sesuai dengan nama yang diinginkan, contohnya '<font color="#ffc0e0">django_project</font>'. Di dalam direktori tersebut, buka *command prompt* (Windows) atau *terminal shell* (Linux/Mac).
2. Buat *virtual environment* Python untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang terdapat pada komputer dengan menggunakan perintah berikut.
<pre style="background-color:#54042b">
python -m venv env 
</pre>

3. Aktifkan *virtual environment* yang telah dibuat dengan menggunakan perintah '<font color="#ffc0e0">env\Scripts\activate.bat</font>'  (Windows) atau '<font color="#ffc0e0">source env/bin/activate</font>' (Linux/Mac). *Virtual environment* yang telah aktif akan ditandai dengan '<font color="#ffc0e0">(env)</font>' pada baris input terminal.
4. Buat file '<font color="#ffc0e0">requirements.txt</font>'  di dalam direktori proyek yang sama dan tambahkan daftar *dependencies* yang dibutuhkan dalam file tersebut. Berikut *dependencies* yang akan digunakan dalam proyek.

<pre style="background-color:#54042b">
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
</pre>

5. Install *dependencies* tersebut pada '<font color="#ffc0e0">requirements.txt</font>' dengan menjalankan perintah berikut:
<pre style="background-color:#54042b">
python -m pip install -r requirements.txt
</pre>

6. Buat proyek Django dengan nama '<font color="#ffc0e0">item_insight</font>' menggunakan perintah berikut:
<pre style="background-color:#54042b">
django-admin startproject item_insight .
</pre>

7. Tambahkan `*` pada `ALLOWED_HOSTS` di dalam `settings.py` yang berada di dalam direktori `inventory_app` untuk mengizinkan akses dari semua host.
```python