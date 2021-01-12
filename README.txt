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
- source code diatur ulang dalam  docker-compose

DOCKER COMPOSE
Docker compose merupakan sebuah tool untuk mendefinisikan dan menjalankan aplikasi container berbasis docker.
dengan menggunakan compose, kita dapat menggunakan file konfigurasi (format YAML), untuk mengkonfigurasi, instance
server berbasis container apa sajakah yang akan kita jalankan. Compose, dapat di start stop dan dipindahkan kemana saja (portable),
asalkan ada docker hypervisor yang berjalan.


CARA MENJALANKAN:
- harus ada aplikasi docker-compose
- di dalam direktori/folder

* docker-compose down  : untuk menstop instances
* docker-compose build : untuk mengcompile Dockerfile menjadi docker image
* docker-compose up : untuk menjalankan instance redis-server dan phonebook-svc (dalam mode foreground)
* docker-compose up -d : dalam mode daemon (detach)
* docker-compose ps --all : untuk melihat instances apa saja yang aktif, dan port berapa yang dapat diakses,

CONTOH OUTPUT:
$ docker-compose ps --all
           Name                         Command               State            Ports
----------------------------------------------------------------------------------------------
phonebookdb_phonebook_1      sh -C start.sh                   Up      0.0.0.0:32000->32000/tcp
phonebookdb_redis-server_1   docker-entrypoint.sh redis ...   Up      6379/tcp

KETERANGAN:
--> instance service phoneboook ini dapat diakses di port 32000
--> instance service redis-server jalan di port 6379, untuk mengetahui IP dari container tersebut,
    jalankan docker inspect phonebookdb_redis-server_1
--> untuk melihat logs dari phonebook service, gunakan
    * docker-compose logs -f phonebook
    atau, gunakan nama instance dockernya (phonebookdb_phonebook_1)
    * docker logs -f phonebookdb_phonebook_1



