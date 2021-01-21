gunakan python3.8 atau yang lebih baru
buatlah dulu lingkungan virtual environment
1. virtualenv venv
2. source venv/bin/activate
3. anda sudah berada dalam linkungan virtualenv
4. jalankan instalasi modul pip install -r requirements
5. jalankan dengan python Service.py
6. lihatlah file testing.txt untuk testing


PERUBAHAN
dalam repository redis-db ini:
- database phonebookdb berubah dari file-based menggunakan redis kv database
- file phonebook.db tidak lagi diperlukan
- implementasi model dalam file PhoneBookModelRedis.py, akses diarahkan ke database redis-server
- Dockerfile disesuaikan, harus menambahkan PhoneBookModelRedis.py ke dalam working directory
- redis-server dijalankan menggunakan instance docker container
- redis-server terhubung ke phonebook service dengan menggunakan isolated network
  dengan nama "phonebookdb-network"

DEPLOYMENT
- Phonebook DB dapat dijalankan oleh penyewa (tenant)
- Satu kesatuan service terdiri dari phonebookdb-service (sebagai frontend) dan redis-server (sebagai record storage)
- Untuk menjalankan, jalankan file run-all.sh
- Dalam run-all.sh, terdapat beberapa langkah
* create network
* run redis-server
* run phonebookdb-service

- Untuk menghentikan jalankan file stop-all.sh




