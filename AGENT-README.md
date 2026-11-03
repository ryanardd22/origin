# Agent di repositori origin

## Mulai melalui chat Codex

Buka `ryanardd22/origin` pada branch yang memuat paket ini, lalu kirim:

> Gunakan $product-hunter. Riset produk FMCG sesuai brief saya: Surabaya, modal total Rp1 juta. Periksa sumber dan supplier yang tersedia. Berikan maksimal tiga pilihan, biaya lengkap dan satu langkah uji bila bukti cukup. Simpan laporan dan ringkas hasilnya. Jangan membeli atau menghubungi supplier.

Jika skill belum muncul, minta Codex membaca `.agents/skills/product-hunter/SKILL.md` langsung. `AGENTS.md` menyediakan instruksi proyek untuk sesi berikutnya.

## Isi paket

- Product Hunter: riset dan shortlist produk; [panduan](ops/PRODUCT-HUNTER.md).
- Origin Growth: scout, matchmaker, offer, outreach, coordinator, analyst; [panduan](ops/README.md).
- Brief produk terpisah di `ops/product-brief.json`; data kontak/strategi lama bukan bukti pasar FMCG.
- CSV operasional adalah template kosong, bukan daftar leads nyata.
- Laporan dan data privat disimpan di jalur yang diabaikan Git; jangan commit kredensial atau data pelanggan.

## Apa yang berjalan

Agent bekerja ketika dipanggil dari chat Codex. GitHub menyimpan instruksi dan runner; tidak ada scheduler, server 24 jam, atau pengiriman pesan otomatis. Akses web bergantung pada sesi Codex/environment, bukan keberadaan file di GitHub.

Enam tes runner dapat dijalankan tanpa koneksi model:

```sh
python3 -m unittest discover -s ops -p test_agent.py -v
python3 ops/agent.py prepare product-hunter --task "Cari tiga kandidat FMCG sesuai modal saya"
```

Mode prepare hanya menyiapkan prompt. Mode run memerlukan Codex CLI, autentikasi, akses model dan kuota; sebelumnya akses endpoint model pada environment ini ditolak proxy 403. Jalur chat digunakan untuk menjalankan agent sekarang.

## Video Shotcraft

Skill `video-shotcraft` dipasang dari [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft), commit upstream `1266a3ec4831289c4d893d42dd5102723658039a`. Sumber dan lisensi upstream dipertahankan di `.agents/skills/video-shotcraft/`.

Contoh pemakaian di Codex:

> Gunakan $video-shotcraft untuk menyiapkan video produk dari aset saya. Baca skill dan panduan instalasi Codex terlebih dahulu.

Skill berfokus pada animasi Remotion berbasis kode, screenshot dan aset. Tidak memerlukan akun Claude untuk rendering lokal. Akses browser/generasi aset/audio atau publikasi luar mengikuti kemampuan dan konfigurasi sesi.

Validasi instalasi: 23 tes helper bawaan lulus; satu frame PNG template dan MP4 H.264 dua detik dengan audio AAC berhasil dirender. Konfigurasi Linux yang diuji memakai Chromium sistem, `--chrome-mode=chrome-for-testing`, dan `--concurrency=1`. Panduan: `.agents/skills/video-shotcraft/CODEX-INSTALL.md`. Ini uji template upstream, bukan video bisnis OriginSYS atau pengujian seluruh fitur/library shot.
