# Product Hunter — cari barang untuk dijual

Agent ini berfokus pada rekomendasi produk, bukan mengubah model perusahaan. Brief awal: FMCG, Surabaya, modal total Rp1 juta, prioritas reseller produk jadi dan pembelian awal kecil.

## Jalankan lewat chat Codex

Di workspace yang memuat berkas ini, tulis:

> Gunakan $product-hunter. Cari produk FMCG untuk saya jual dengan modal total Rp1 juta. Periksa sumber dan supplier yang bisa diakses. Berikan maksimal tiga pilihan, hitung modal kas serta biaya per order, lalu pilih satu eksperimen jika buktinya cukup. Jika tidak ada akses web, tandai semuanya sebagai hipotesis dan jangan mengarang harga/supplier. Simpan hasil dan ringkas di chat. Jangan membeli atau menghubungi supplier dulu.

Jika skill belum muncul, minta Codex membaca `.agents/skills/product-hunter/SKILL.md` langsung. Sesi Codex harus memuat perubahan lokal ini; menghubungkan GitHub tidak otomatis mengunggah file.

## Via terminal

```sh
python3 ops/agent.py prepare product-hunter --task "Cari tiga kandidat FMCG sesuai modal saya"
```

Mode prepare menyusun prompt, tidak melakukan riset. Mode run juga tersedia jika Codex CLI dan akses model bekerja, tetapi endpoint CLI pada environment ini sebelumnya ditolak proxy 403. Gunakan chat sebagai jalur utama. Agent berjalan saat dipanggil, bukan otomatis setiap hari atau 24 jam.

## Standar hasil

Harga listing harus punya SKU, ukuran/varian, kuantitas dan tanggal. Stok dan quote supplier belum terkonfirmasi hanya karena ada listing. Angka yang tidak dapat diketahui tetap kosong, bukan nol. Sampel dan pembelian ulang tidak boleh diklaim sebelum benar-benar terjadi.

Urutan keputusan: hipotesis kategori → kandidat bersumber → layak uji sampel → layak uji jual. Tidak perlu menghabiskan modal untuk mencapai tahapan berikutnya; pemilik tetap memutuskan pembelian.

Riset internet saat ini bergantung pada tool dan network environment yang tersedia. Jika akses belum terbuka, hasil awal hanya dapat berupa kandidat kategori dan rencana pembuktian. Agent tidak meminta token baru untuk mengatasi penolakan kebijakan network.
