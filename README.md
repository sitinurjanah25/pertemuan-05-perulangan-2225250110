# Pertemuan 05 Perulangan Python

Nama: Siti Nurjanah  
NIM: 2225250110  
Kelas: 3E

## Tujuan

Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif.

## Cara Menjalankan

Jalankan program Kuis 2 melalui terminal:

```text
python3 kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

1. Memasukkan suku pertama `a`.
2. Memasukkan beda `d`.
3. Memasukkan banyak suku `n`.
4. Memvalidasi nilai `n` menggunakan `while` sampai bernilai positif.
5. Menggunakan `for` untuk menghasilkan setiap suku deret aritmetika.
6. Menambahkan setiap suku ke variabel `total`.
7. Menampilkan setiap suku dan jumlah seluruh suku.

## Hasil Pengujian

| No. | Input | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|---|
| 1 | a=2, d=3, n=5 | Suku: 2.00, 5.00, 8.00, 11.00, 14.00; Jumlah = 40.00 | Suku: 2.00, 5.00, 8.00, 11.00, 14.00; Jumlah = 40.00 | Berhasil |
| 2 | a=10, d=-2, n=4 | Suku: 10.00, 8.00, 6.00, 4.00; Jumlah = 28.00 | Suku: 10.00, 8.00, 6.00, 4.00; Jumlah = 28.00 | Berhasil |
| 3 | a=1.5, d=0.5, n=3 | Suku: 1.50, 2.00, 2.50; Jumlah = 6.00 | Suku: 1.50, 2.00, 2.50; Jumlah = 6.00 | Berhasil |

## Refleksi

Kesalahan yang perlu diperhatikan dalam perulangan adalah menempatkan `total = 0` di dalam loop. Jika `total` diinisialisasi kembali menjadi 0 setiap kali perulangan berjalan, hasil penjumlahan tidak akan terakumulasi dengan benar. Cara memperbaikinya adalah menempatkan `total = 0` sebelum loop dimulai sehingga nilai `total` dapat menyimpan hasil penjumlahan dari setiap suku.

## Catatan Pengujian

Program telah diuji menggunakan beberapa nilai input dan menghasilkan keluaran sesuai dengan yang diharapkan.

## Refleksi

Dalam perulangan, variabel penghitung atau akumulator harus ditempatkan dengan tepat. Jika `total = 0` diletakkan di dalam loop, nilai sebelumnya akan kembali menjadi 0 sehingga hasil penjumlahan tidak terakumulasi dengan benar.

## Status Pengujian

Semua program latihan dan Kuis 2 telah diuji dan dapat berjalan sesuai dengan ketentuan tugas.
