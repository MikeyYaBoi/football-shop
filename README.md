<details>
<summary>TUGAS 2</summary>
Untuk membuat proyek Django ini, pertama saya membuat virtual environment di terminal. Lalu saya menginstal beberapa dependancies yang dibutuhkan dalam proyek sesuai dengan langkah pada tutorial 0. Lalu saya buat proyek tugas 2 ini dengan nama football_shop.
Saya membuat aplikasi "main" pada proyek dengan menjalankan perintah py manage.py startapp main pada terminal dalam direktori proyek dan virtual environment. Lalu pada file settings.py di direktori proyek saya daftarkan aplikasi 'main' ke dalam variabel INSTALLED_APPS.
Routing URL untuk mengakses aplikasi main dilakukan dengan cara pergi ke file urls.py di direktori proyek, impor fungsi include dari django.urls, lalu pada variabel urlpatterns saya tambahkan kode path('', include('main.urls'))
Saya membuat model dengan cara membuat class Product yang inherit dari models.Model lalu memberikan atribut-atribut seperti name, price, description, thumbnail, category, dan is_featured sesuai dengan tipe yang diminta tugas.
Pada views.py di direktori main, saya buat fungsi show_main. Fungsi berisi dictionary nama, harga, dan dekripsi sepatu. Fungsi akan mereturn dengan memanggil fungsi render dari library django.shortcuts yang akan mengisi slot-slot pada template main.html dengan value dari context tersebut.
Saya membuat file urls.py pada direktori main berisi variabel urlpatterns yang menyimpan path ke views.py agar bisa memanggil fungsi show_main sebelumnya.
Deployment ke PWS saya lakukan sama persis dengan langkah-langkah pada sesi tutorial sebelumnya.
settings.py adalah pusat konfigurasi proyek Django. Intinya: semua pengaturan global aplikasi ada di sana dan dieksekusi sebagai modul Python saat Django dijalankan.
Migrasi bekerja dengan cara menulis/mengubah model (models.py) di app. Lalu jalankan py manage.py makemigrations di terminal dalam virtual environment. Django membandingkan state model saat ini dengan snapshot terakhir, lalu membuat berkas migrasi di direktori migrations. Lalu jalankan py manage.py migrate. Ini menerapkan migrasi ke database: Django menjalankan operasi yang sesuai dan mencatat migrasi yang sudah dijalankan di tabel django_migrations.
Django sering dipilih karena menyediakan banyak fitur built-in (ORM, auth, admin UI, forms, i18n, sessions, caching, dan lain-lain). Jadi pemula dapat membangun aplikasi lengkap tanpa menambahkan banyak paket dari awal. Struktur proyek dan pola kerja terorganisir (models, templates, views) sehingga pembelajaran arsitektur web jadi lebih mudah.
</details>

<details>
<summary>TUGAS 3</summary>
Data delivery diperlukan untuk dapat menerima, mengelola, dan mengirimkan data dengan cepat, tepat, dan aman.
Menurut saya, JSON lebih baik dari pada XML karena sintaksnya yang sederhana yaitu berupa pasangan key-value yang merepresentasikan sebuah objek yang kemudian disimpan dalam sebuah array. XML memiliki sintaks seperti HTML dalam penulisannya sehingga cenderung lebih sulit dibaca. Oleh karena itu, JSON lebih populer dibanding XML.
Fungsi is_valid bertujuan untuk memvalidasi data yang diinput pengguna ke bagian form. 
csrf_token berguna untuk mencegah serangan Cross-Site Request Forgery di mana penyerang menipu pengguna untuk mengirim request berbahaya ke website dengan diam-diam. Tanpa token, proteksi dari Django akan menolak request dari form POST. Penyerang dapat memanfaatkannya dengan mengarahkan pengguna ke halaman URL palsu berisi kode tertentu dari pelaku. Setelah URL dibuka, kode tersebut akan langsung berjalan, seperti mengubah kata sandi akun, transfer uang, atau perintah lainnya.
Untuk melihat objek yang telah ditambahkan ke dalam database, pada views.py saya membuat fungsi show_xml & show_json yang menampilkan semua objek dalam format xml dan json, serta show_xml_by_id & show_json_by_id yang masing-masing akan menampilkan sebuah objek spesifik dalam xml dan json berdasarkan id objek. Saya memanggil fungsi serialize dari modul serializer untuk menerjemahkan objek model ke dalam format XML dan JSON, kemudian fungsi akan mengembalikan respons kepada pengguna dengan memanggil fungsi HttpResponse. Pada fungsi show_xml_by_id dan show_json_by_id, jika objek yang dicari tidak ada, maka fungsi akan mengembalikan response berupa eror tipe 404.
Routing keempat fungsi pada views.py saya lakukan dengan cara mengimpor fungsi-fungsi tersebut ke dalam urls.py. Lalu rute URL mengaksesnya saya buat jadi "url-deployment-pws/xml/" untuk format XML dan "url-deployment-pws/json" untuk JSON. Mengakses satu objek spesifik dengan id-nya saya buat menjadi "../xml/<uuid:product_id>/" dan "../json/<uuid:product_id>/" di mana tag uuid berisi id objek yang ingin dilihat.
Pada halaman utama main.html saya membuat tombol '+ Add Product' sebagai hyperlink yang memanggil fungsi create_product lalu mengarah ke URL 'url-pws/create_product' yang menampilkan create_product.html untuk menambah produk baru. Selain itu, main.html menampilkan setiap produk yang ada di database di bawah tombol Add Product. Daftar produk yang ditampilkan bisa dilihat detailnya dengan membuat hyperlink pada nama produk yang bisa diklik dan tombol Read More di bawah thumbnail produk. Kedua hyperlink melakukan hal yang sama yaitu memanggil fungsi show_product yang mengarah URL '../product/[id produk]/' yang akan menampilkan product_detail.html sesuai dengan id produknya.
Halaman form dan detail produk saya buat sama seperti langkah-langkah yang diberikan dari tutorial 2.

URL access on Postman:
https://drive.google.com/drive/folders/1QVTYtCZdyCLBZqRP3xho83nVrNpFqPik?usp=sharing
</details>

<details>
<summary>Tugas 4</summary>
Django AuthenticationForm adalah sebuah class pada Django yang berfungsi untuk membuat fitur dan form/halaman login agar pengguna dapat masuk ke dalam situs web.
Kelebihannya yaitu: 1. Form bawaan Django yang bisa langsung diimplementasikan ke dalam web. 2. Keamanan yang terjamin secara default, seperti dalam password hashing dan session management (aktif/tidak aktifnya user). 3. Integrasi dengan autentikasi Django, di mana bisa langsung bekerja dengan model User dari Django dan restriksi halaman situs dengan decorator @login_required. 4. Penanganan eror otomatis seperti pengecekan keberadaan user dan verifikasi username/password yang salah tanpa menulis logika sendiri.
Kekurangannya yakni: 1. Tampilan yang sederhana tanpa ada styling dan semacamnya. 2. Sistem autentikasi standar (username & password) saja. 3. Kurang fitur autentikasi lebih seperti 2-factor authentication, "Remember me", dan login dengan akun sosial seperti Google dan Facebook.

Autentikasi adalah proses mengetahui siapa diri Anda (user), sedangkan otorisasi adalah proses mengetahui apa saja kewenangan/yang dapat dilakukan oleh user.
Autentikasi (bawaan) di Django: Model User, Fungsi login, logout, dan authenticate, class AuthenticationForm.
Otorisasi di Django: Decorator @login_required yang merestriksi halaman situs html untuk user yang telah login, model yang dibuat memiliki permission otomatis (seperti add, change, delete, view).

Kelebihan Cookie: Mudah digunakan karena data langsung tersimpan di browser, otomatis terkirim ke server pada setiap request serta bertahan lama sehingga cocok untuk fitur seperti "remember me" atau preferensi pengguna. Data disimpan di sisi client maka server tidak perlu menyimpan state tambahan. Bisa diakses JavaScript Memudahkan kustomisasi oleh user.
Kekurangan Cookie: Ukuran maksimal cookie sebesar 4KB. Data mudah dibaca oleh user dan rawan kena serangan XSS jika tidak dienkripsi. Setiap request akan memakan lebih banyak bandwidth dan memperlambat request. Cookies dapat dimatikan kapan saja oleh user dan dihapus.
Kelebihan Session: Data tersimpan dengan aman di dalam server. Dapat menampung data yang sangat besar dan kompleks. 
Kekurangan Session: Beban server lebih besar karena menyimpan semua data state untuk menghandle setiap request dari user. Manajemen ekstra pada setiap session user. Tetap bergantung pada cookies seperti untuk mengirimkan session ID, sehingga rentan dicuri atau dapat tidak bekerja jika dimatikan oleh user.

Cookies tidak sepenuhnya aman karena dapat dibaca dan dimodifikasi di sisi client. Cookies juga dapat dicuri oleh hacker melalui serangan seperti Cross-Site Scripting yang mencuri cookie melalui skrip berbahaya, Cross-Site Request Forgery di mana user mengirimkan request palsu berbahaya oleh hacker, dan Man-in-the-middle yang mencuri cookies ketika website tidak menggunakan protokol HTTPS. 
Cara Django menanganinya yaitu: menyertakan csrf_token ke dalam semua form di html, mengatur cookie session dengan 'httponly=True' agar tidak dapat diakses via JavaScript, atur 'SESSION_COOKIE_SECURE' dan 'CSRF_COOKIE_SECURE' sehingga cookie hanya dikirim melalui HTTPS.

Implementasi fitur register saya lakukan dengan terlebih dahulu mengimpor UserCreationForm, yaitu class bawaan Django untuk membuat formulir registrasi akun baru user. Saya membuat fungsi register() di views.py pada direktori main. Di dalamnya terdapat instance UserCreationForm kosong bernama form. Saat user memberikan username dan password untuk akun barunya, user mengirimkan HTTP request POST ke server lalu request akan digunakan untuk membuat instance UserCreationForm baru meng-overwrite instance pada variable form. Jika username dan password akun sesuai aturan (bawaan dari Django), data akan disimpan ke dalam database dan user diarahkan kembali ke halaman login bersamaan dengan pesan bahwa akun telah berhasil dibuat dengan memanggil fungsi messages.success(). Jika isi form registrasi tidak sesuai aturan, user tetap berada di halaman register dan mendapat pesan yang memberitahu ketentuan username/password yang belum benar.
Halaman register saya ada di file register.html pada main/templates. File meng-extend base.html di direktori utama, judulnya Register, elemen form dibuat dalam bentuk tabel dengan tag {{ from.as_table }}. Juga terdapat tag {% csrf_token %} untuk melindungi dari serangan CSRF dan bullet list berisi aturan username dan password untuk akun baru. Setelah itu, saya routing dengan pergi ke main/urls.py lalu impor fungsi register dari views.py dan tambahkan 'path('register/', register, name='register')' ke dalam list urlpatterns.

Fitur login saya buat dengan mengimpor AuthenticationForm, authenticate, dan login pada views.py. Saya buat fungsi login_user(). Fungsi menerima request POST dari user yaitu input username dan password akunnya. Dari request, fungsi membuat instance AuthenticationForm bernama form dengan atribut dari request. Jika username dan password benar, fungsi akan mengambil akun yang sesuai dari database, memanggil fungsi login(request, user) yang akan membuat session baru buat pengguna lalu mereturn fungsi redirect() ke halaman utama website. Jika input login salah, maka website akan tetap di halaman login.
Halaman login saya yaitu login.html pada main/templates. Isinya mirip dengan halaman register.html hanya beda di bagian bawah halaman terdapat hyperlink untuk membuat akun baru. Terakhir, saya hubungkan halaman ini pada main/urls.py dengan menambahkan 'path('login/', login_user, name='login')' pada urlpatterns.

Pembuatan fitur logout saya buat dengan terlebih dulu mengimpor fungsi logout pada views.py. Saya buat fungsi baru logout_user() yang di dalamnya akan memanggil fungsi 'logout(request)' dan mereturn fungsi redirect() yang akan mengarahkan ke halaman login. Pada main.html saya tambahkan button 'Logout' berupa hyperlink yang isinya {% url 'main:logout' %} yang secara dinamis mengarah ke path URL pada main/urls.py dengan paramater nama 'logout'. Terakhir, pada urls.py tersebut saya tambahkan 'path('logout/', logout_user, name='logout')' agar bisa menjalankan hyperlink button tadi.

Penerapan Cookies
Pada views.py saya import datetime, HttpResposeRedirect, dan reverse. Pada fungsi login_user() di blok 'if form.is_valid()', saya buat variabel response yaitu instance HttpResponseRedirect(reverse("main:show_main")). Pada response disimpan cookie saat ini user login bernama 'last_login' dengan fungsi set_cookie(). Variabel response direturn menggantikan return sebelumnya lalu akan balik ke halaman utama.
Pada dictionary context saya tambahkan key='last_login' dengan value=request.COOKIES.get('last_login', 'Never') yang mengambil nilai cookie 'last_login'.
Saya buat variabel response yang sama di fungsi logout_user(). Saya panggil fungsi delete_cookie() untuk menghapus cookie 'last_login' setelah user logout. Pada key 'name' valuenya saya buat 'request.user.username' untuk memunculkan akun yang sedang login saat ini. Fungsi mereturn response.
Halaman main.html saya tampilkan waktu terakhir login user dengan tag {{ last_login }} yang diisi oleh key 'last_login' dari login_user().

Saya menghubungkan model Product dengan User dengan cara mengimpor class User dari Django. Pada model Product saya tambahkan atribut user: 'models.ForeignKey(User, on_delete=models.CASCADE, null=True)'. Atribut ini akan mengikat satu instance Product dengan satu instance User saja. Product yang tidak punya User akan tetap ada di database melalui 'null=True' dan akun User yang dihapus akan menghapus semua Product yang dimiliki melalui 'on_delete=models.CASCADE' pada atribut user. Perubahan models.py saya migrate di terminal.
Pada views.py di fungsi create_product() blok 'if' saya buat variable product_entry yang menyimpan input produk baru yang ingin dijual. Lalu fied user dari product_entry tersebut akan diisi dari request.user (user yang sedang aktif).

<details>
<summary>TUGAS 5</summary>
Pada halaman login, saya beri latar abu-abu cerah penuh (bg-gray-50). Saya wrapping dalam kontainer luar lebarnya utuh dan tinggi sama dengan viewport, sehingga card dapat dipusatkan vertikal. Card login di tengah secara vertikal dan horizontal. Padding luar untuk memberikan ruang dari tepi layar. Lebar card dikasih batas di layar besar, tetapi tetap responsif di layar kecil. Card latarnya putih rounded border warna abu-abu. Judul teks rata tengah ukuran 2xl dan dibuat bold. 

Urutan prioritas CSS selector: 1. Inline style (di dalam style tag) 2. ID selector (diawali #) 3. Class selector (diawali .) 4. Element selector

Responsive design penting karena ada beberapa manfaat yang diberikan, yaitu pengguna mengakses situs dari berbagai perangkat, tampilan tetap nyaman dan mudah dibaca di layar kecil, memudahkan koding desain untuk semua ukuran layar, situs yang mobile-friendly lebih mudah muncul di search engine, dan mengurangi bounce rate. Contoh aplikasi yang punya responsive design: Youtube, Gojek, Tokopedia, X. Contoh aplikasi yang belum: CodingBat, Internet Archive, SIAK-NG.

Perbedaan margin, border, padding:
Margin: Area transparan di luar border yang memberi jarak antar elemen.
Border: Garis pembatas di antara margin dan padding.
Padding: Area transparan di dalam elemen (antara konten website dan border).
Contoh implementasi: 
.box {
  margin: 20px;     /* Jarak dari elemen lain */
  border: 2px solid black; /* Garis pembatas */
  padding: 15px;    /* Jarak konten dari border */
}

Flexbox adalah sistem layout 1 dimensi mengatur baris atau kolom yang digunakan untuk mengatur dan meratakan elemen secara dinamis.
Kegunaannya: Menyusun elemen secara horizontal atau vertikal, mengatur jarak dan perataan antar elemen dengan mudah dalam kontainer, menyesuaikan lebar/tinggi elemen anak secara fleksibel. Flexbox cocok untuk komponen kecil seperti navbar, card, atau form.
CSS Grid Layout adalah sistem layout 2 dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom sekaligus. Sistem ini ideal untuk layout halaman utama (header, sidebar, content, footer), dapat menentukan ukuran kolom/baris dengan mudah, lebih presisi untuk tata letak kompleks.


</details>
