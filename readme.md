# Integra ITS Scrapping

## Deskripsi
Sebuah script untuk scrapping dan otomatisasi penggunaan fitur
di Integra ITS (https://integra.its.ac.id). 

P.S
This script means NO HARM at all, just an experiment. Always use this carefully.

Saya tidak bertanggung jawab apabila ada masalah birokrasi atau pembekuan akun atas penggunaan
script ini secara berlebihan

## How To

### Run It
Buatlah file `credential.json` yang berisikan NRP dan Password anda dengan format berikut

```
{
    "userid" : "NRP ANDA",
    "password" : "PASSWORD ANDA
}
```

Pastikan anda sudah menginstall modul - modul berikut
* requests - Untuk melakukan HTTP Request
* json - Untuk mengolah data dalam format json
* BeautifulSoup 4 - Untuk melakukan parsing data dalam format HTML

Ini adalah script dengan bahasa pemrograman Python 2.7, anda bisa menjalankannya dengan
melakukan perintah berikut di terminal

```
python <nama file>.py
```

### Use Specific Function
#### integra.py
Pada script `integra.py` tersedia 2 fitur yang berfungsi dengan baik

* Mendapatkan list ranking IPK
* Mendaftarkan SKEM

Untuk memilih fitur yang akan anda gunakan, cukup uncomment fungsi terkait
dan comment fungsi yang tidak diperlukan.

Misalkan anda ingin mendapatkan ranking IPK, maka cukup uncomment fungsi `get_ipk_rank()`
dan comment fungsi yang lain (soon will update the feature to choose specific function).

#### stalking.py
Terdapat file script lain yaitu `stalking.py` yang berguna untuk melihat daftar mata kuliah yang diambil oleh
seorang mahasiswa tertentu.

Fungsi `login_integra(s)` adalah fungsi untuk mensimulasikan proses login ke integra,
jadi jangan pernah menonaktifkan fungsi ini pada `integra.py` maupun `stalking.py`

## How Does It Work?

Script ini mensimulasikan browser anda ketika menggunakan website Integra ITS dengan cara menyimpan
tiap cookie yang anda dapatkan di setiap gate.
