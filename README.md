# **Item Insight**

**Pemrograman Berbasis Platform**<br/>
**Tugas 2: Implementasi Model-View-Template (MVT) pada Django**<br/>

**Author**<br/>
Shanti Yoga Rahayu<br/>
2206082360<br/>
PBP D<br/>

Tautan menuju aplikasi Adaptable yang sudah melalui tahap deployment dapat diakses melalui [link ini](https://item-insight.adaptable.app/main/).

## **Membuat Sebuah Proyek Django Baru**
1. Buat sebuah direktori baru sesuai dengan nama yang diinginkan, contohnya `item_insight`. 
2. Di dalam direktori tersebut, buka *command prompt* (Windows) atau *terminal shell* (Linux/Mac).
3. Buat *virtual environment* Python untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang terdapat pada komputer dengan menggunakan perintah berikut.
```
python -m venv env 
```
4. Aktifkan *virtual environment* yang telah dibuat dengan menggunakan perintah berikut. *Virtual environment* yang telah aktif akan ditandai dengan `(env)` pada baris input terminal.
- Windows
```
env\Scripts\activate.bat
```
- Linux/Mac
```
source env/bin/activate
```

5. Buat file `requirements.txt`  di dalam direktori proyek yang sama dan tambahkan daftar *dependencies* yang dibutuhkan dalam file tersebut. Berikut *dependencies* yang akan digunakan dalam proyek.

```txt
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

6. Install *dependencies* tersebut pada `requirements.txt` dengan menjalankan perintah berikut.
```
python -m pip install -r requirements.txt
```

7. Buat proyek Django dengan nama `item_insight` menggunakan perintah berikut.
```
django-admin startproject item_insight .
```

8. Tambahkan `*` pada `ALLOWED_HOSTS` yang terdapat di dalam `settings.py` yang berada di dalam direktori `item_insight` untuk mengizinkan akses dari semua host. Perlu diingat untuk menggunakan pengaturan ini dengan bijak dan hanya dalam situasi tertentu, seperti saat melakukan uji coba atau tahap awal pengembangan
```python
...
ALLOWED_HOSTS = ["*"]
...
```

9. Pastikan bahwa berkas 'manage.py' terdapat pada direktori yang aktif pada shell kamu saat ini. Di dalam direktori utama, buka kembali *command prompt* atau *terminal shell*. Jalankan server dengan perintah berikut.
```
python manage.py runserver
```

10. Akses http://localhost:8000 di peramban web untuk melihat animasi roket yang menandakan bahwa pembuatan aplikasi Django telah berhasil.
11. Hentikan server dapat dilakukan dengan menekan tombol `Ctrl+C` pada *command prompt* atau *terminal shell*. 
12. Nonaktifkan *virtual environment* dengan menggunakan perintah `deactivate`.
> [!NOTE]
> Buat `.gitignore` yang berisi file yang tidak diperlukan agar tidak memenuhi space.
Isi dari `.gitignore` adalah sebagai berikut.

```.gitignore
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

## **Membuat Aplikasi dengan Nama Main Pada Proyek Item Insight**
1. Buka command prompt pada direktori utama `item_insight`.
2. Aktifkan virtual environment dengan perintah berikut.
```
env\Scripts\activate.bat.
```
2. Buat aplikasi main dengan perintah berikut sehingga terbentuk direktori baru dengan nama main yang akan berisi struktur awal untuk aplikasi.
```
python manage.py startapp main
```
3. Daftarkan aplikasi main ke proyek dengan membuka berkas `settings.py` dalam direktori proyek `item_insight` dan tambahkan `'main'` pada variabel INSTALLED_APPS.
```
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

## **Melakukan Routing Pada Proyek untuk Menjalankan Aplikasi Main**

## **Membuat Model Pada Aplikasi `Main` dengan Nama Item dan Memiliki Atribut**
1. Buka berkas `models.py` pada direktori aplikasi `main`.
2. Ubah file `models.py` yang terdapat di dalam direktori aplikasi `main` tersebut untuk mendefinisikan model dengan nama `ItemStore` dan memiliki atribut wajib sebagai berikut.
* `name` sebagai nama item dengan tipe `CharField`.
* `amount` sebagai jumlah item dengan tipe `IntegerField`.
* `description` sebagai deskripsi item dengan tipe `TextField`.<br/>
Tambahkan atribut lainnya sesuai dengan apa yang diinginkan, seperti `price` dan `category`. 
2. Isi file `models.py` dengan kode berikut.
```python
from django.db import models

class ItemStore(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.BigIntegerField()
    category = models.CharField(max_length=255)
```

3. Jalankan perintah `python manage.py makemigrations` untuk membuat migrasi model. `makemigrations` akan membuat berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data.

4. Jalankan perintah `python manage.py migrate`.`migrate` akan mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data.

> [!IMPORTANT]
> Setiap kali melakukan perubahan pada model, seperti menambahkan atau mengubah atribut, perlu melakukan migrasi untuk merefleksikan perubahan tersebut.