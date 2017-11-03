# CIDR-calculator
---
## Petunjuk penggunaan program
* Buka terminal pada directory __Makefile__
* Ketikan query __make run__
* Masukan __NIM__

## Penjelasan singkat proses
* __Phase 1__

Pada phase 1, kita akan memberikan input sebuah subnet yaang valid.
Semua inputan kita akan diperiksa dengan mencocokkan n bit pertama
subnet yang kita input (tanpa CIDR) dengan n bit pertama dari host
dimana n adalah CIDR yang kita input. Jadi benar tidaknya input kita
diperiksa dengan CIDR input yang menjadi jumlah bit pertama yang akan
diperiksa dari host dan subnet input.
* __Phase 2__

Pada phse 2, CIDR akan menjadi fokus utama perhitungan. Panjang sebuah subnet adalah 32 bit. Selain menunjukkan kelas, CIDR akan menginformasikan berapabit yang telaah dipakai, misalnya 20. Otomatis bit yang tidak terpakai (sisanya) adalah 12 bit lagi (agar tetap menjadi 32 bit). Setelah itu akan di hitung jumlah maksimumdari host yang dapat ditempati yaitu 2^(32-CIDR).
* __Phase 3__

Pada phase 3, baik host maupun subnet(tanpa blok CIDR) akan diubah menjadi bit sepanjang 32 karakter bit. Kemudian akan dibandingkan n bit pertama dari bit host maupun subnet dimana n adalah CIDR (0-32). Apabila n bit pertamanya sama, program akan melempar nilai True (dalam hal ini 'T') sedaangkan jika ada 1 saja yang tidak sama program akan melempar nilai False (dalam hal ini 'F').
