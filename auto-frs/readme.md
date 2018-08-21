# Integra ITS Auto FRS Script
Made by [Rogo Jagad Alit](https://www.linkedin.com/in/rogo-jagad-alit-a58997114/)

### Untuk apa?
Dengan menggunakan script ini, anda dapat melakukan pengisian FRS dengan **SANGAT CEPAT**. Sehingga kemungkinan untuk mendapatkan mata kuliah favorit pun menjadi **SANGAT BESAR**
### Disclaimer:
- Use it with your own risk. Saya tidak bertanggung jawab jika terjadi sesuatu pada akun Integra anda akibat penggunaan script ini.
- Script ini dikembangkan dan telah ditest pada lingkungan kerja **Linux Ubuntu**. Jika anda menjalankan pada lingkungan kerja selain itu, **saya tidak menjamin keberhasilannya**.
- Script ini bekerja dengan baik pada masa FRS Semester Gasal 2018/2019
### Prerequisites:
- Pastikan host tempat anda menjalankan script ini telah tersedia bahasa pemrograman **Python 2.7** (kemungkinan di masa depan akan saya upgrade menggunakan Python 3)
- Telah terinstall **Python library manager** seperti Pip, Anaconda dan sejenisnya untuk memudahkan pemasangan library yang dibutuhkan
- Install library berikut ini dengan Python library manager kesukaan anda : **Beautiful Soup (Bs4)**, **Requests**, **lxml**, **json**
### How to Use?
1. Clone repo ini
2. Lakukan langkah yang disebutkan pada bagian **Prerequisites**
3. Rename file `credentials.json.example` menjadi `credentials.json`
4. Isi NRP kalian pada bagian `userid` dan password kalian pada bagian `password`
5. Buka file `auto-frs.py`
6. Pada fungsi `matkulList`, isikan kode matkul yang kalian inginkan di bagian `listOfMatkul` (lihat bagian **Panduan Kode Matkul** untuk membuat kode matkul)
7. Jalankan `python auto-frs.py` di terminal anda

### Panduan Kode Matkul
Format : `{kode mata kuliah}|{kelas}|{tahun kurikulum}|{kode departemen}|0`

* Kode mata kuliah : Dapat dilihat di Silabus Kurikulum departemen anda. Contoh: IF4954 (Robotika)
* Kelas : Kelas mata kuliah (diisi dengan `_` jika hanya terdapat satu kelas)
* Tahun Kurikulum : 2018 (yang digunakan saat ini)
* Kode Departemen : 51100 (Departemen Informatika)

**BINGUNG?** Anda bisa melakukan `Inspect Element` di halaman FRS untuk mengetahui kode matkul terkait

### Sedikit Tips dan Trick
Anda bisa menjalankan script ini sepanjang waktu dan dimanapun. Namun, saya menyarankan untuk menjalankan script ini di komputer yang bisa online 24 jam dan memiliki koneksi internet untuk mendapatkan **HASIL MAKSIMAL**.