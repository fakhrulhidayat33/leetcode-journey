diawali dengan memilih contoh-contoh bilangan romawi

saya mencoba menggali beberapa kemungkinan yang akan terjadi

pertama kasus umum

MMDCCXXXIX
yang minim dengan pengurangan

lalu kasus ribet
MCMXCIV
yang menggunakan banyak pengurangan

di awali dengan menuliskan dictionary dengan key simbol dan valuenya nilai dalam integer
dan masuk ke looping terhadap s-nya

untuk proses penambahan diloopingnya saya mulai melihat pola, pertama
saya melihat pola yang muncul bilangan-bilangan ini memiliki tingkatan
sehingga saya berniat mengubah value dari dictionary tadi menjadi tuple (nilai, tingkatan).

Dipikir lagi, tingkatan di sini terlalu boros karena saya menemukan pola yang lebih sederhana pergerakan yaitu
1) turun tingkatan
2) di tingkatan yang sama
3) naik tingkatan

jadi saya berniat mengembalikan dictionary ke awal dan menambahkan boolean untuk dijadikan switch-er nya.
karena pola nya sudah terlihat sya memutuskan untuk membuat awalan polanya pasti turun dengan membuat nilai sebelumnya jelas lebih dari semuanya, yakni 10.000. lalu mulai mengulik bagian di dalam looping.

jadi saya memisahkan dua tahap besar dalam melakukan tugas di dalam looping
1) pemilihan switcher dilihat dari keadaan
2) aktivitas sesuai dengan switchernya

ketika melihat program yang selesai saya tulis, saya melihat tahap 1 cuman melakukan 1 tugas yakni pemilihan switcher dan tahap 2 langsung mengeksekusi penambahan sesuai dengan switcher yang terpilih, jadi saya memutuskan untuk menggabung tahap 1 dan 2, tapi mempertahankan switchernya karena di awal switcher ini saya niatkan untuk
1) pemilih tugas
2) penentu langkah akhir

tapi melihat pola untuk mengawali looping dengan memastikan turun, bagaimana jika saya memastikan polanya juga akan turun.

jadi saya menghapus switcher, menambahkan key 'S' dengan nilai 0 lalu menambahkan 'S' ke dalam string yang akan diproses dalam loopping

saya pun menjalankan program dan mendapatkan error karena hasilnya selalu memiliki 10.000, hasil dari penentu pola diawal.

untuk menyelesaikan error tersebut, maka hasil akhirnya saya kurangi dengan 10.000.

Melalui program ini saya memperoleh hasil berikut
runtime: 15 ms | Beats 24.88%
memory: 12.30 MB | Beats 91.62%
 (May, 13th 2026 05:57 GT+7)
