# OriginSYS Agent Desk

Enam peran agent, satu pipeline, pencatatan CSV. Ini paket kerja Codex yang dipanggil saat dibutuhkan, **bukan enam bot yang sudah berjalan 24 jam**. Tidak ada pesan, publikasi, pembayaran, atau transaksi yang dijalankan otomatis. Kota awal: Surabaya, sesuai jawaban pemilik. Radius layanan belum dipilih; belum ada relasi penyedia menurut pemilik. Daftar pembeli dan penyedia belum terisi.

## Pakai di Codex sekarang

Pilih repositori origin dan tulis:

> Gunakan $origin-growth. Jalankan scout dan matchmaker untuk [kota/radius]. Cari bukti kebutuhan coffee break kantor dan kandidat penyedia dari sumber yang dapat diakses. Simpan sumber/tanggal, bedakan kandidat dan terverifikasi. Buat draft saja, jangan menghubungi siapa pun. Lalu minta offer menilai ekonomi transaksi dan analyst menyusun tiga tugas berikutnya.

Skill disimpan di `.agents/skills/origin-growth/SKILL.md`. Jika sesi belum mendeteksi skill baru, sebutkan path itu secara langsung atau mulai sesi baru. Tidak perlu memasang API key untuk membaca prompt ini di Codex yang sudah terautentikasi.

## Runner terminal

Python 3 standar cukup untuk menyiapkan prompt:

```sh
python3 ops/agent.py prepare scout --task "Susun rencana riset coffee break untuk kota yang belum ditentukan"
python3 ops/agent.py prepare analyst --task "Audit pipeline saat ini dan tulis tiga pekerjaan berikutnya"
```

Mode `run` memerlukan Codex CLI terpasang, login yang valid, akses model, dan kuota. Ini bisa menggunakan kuota/biaya akun sesuai paket; tidak dijadwalkan otomatis.

```sh
python3 ops/agent.py run analyst --task "Baca CSV saat ini. Laporkan bukti yang ada, hal yang belum diketahui, dan tiga pekerjaan berikutnya."
```

Runner meneruskan prompt ke `codex exec` melalui stdin, memakai sandbox read-only, menyimpan jawaban final ke `ops/runs/` dengan nama unik. Timeout 10 menit. Exit nonzero atau tanpa laporan bukan sukses. `.partial.md` bukan laporan selesai. Pengaturan tool/auth Codex tetap mengikuti instalasi pengguna; prompt bukan sistem pembatas izin integrasi eksternal. Instruksi default semua peran hanya riset dan draft.

Mode prepare dan pengujian runner lokal sudah dijalankan. Mode run kemudian dicoba dan gagal karena endpoint model ditolak proxy CONNECT 403; tidak ada hasil analisis dari jalur CLI. Agent dalam chat Codex sudah dijalankan sebagai jalur yang tersedia; baca CHAT-START.md dan laporan aktual di ops/runs. Agent tidak memiliki akses Instagram/WhatsApp/email otomatis hanya karena GitHub disambungkan.

## Peran dan handoff

| Peran | Masukan | Hasil selesai |
| --- | --- | --- |
| scout | kota, segmen, sumber publik | kandidat bersumber + bukti kebutuhan + pertanyaan kualifikasi |
| matchmaker | kebutuhan, quote penyedia | opsi penyedia + status konfirmasi + kekurangan |
| offer | kebutuhan dan quote | proposal + fee + biaya + tanggung jawab |
| outreach | fakta dan proposal | pesan personal siap ditinjau + satu follow-up |
| coordinator | persetujuan pembeli/penyedia | lembar order + konfirmasi yang masih kurang |
| analyst | kejadian aktual dan biaya | pipeline + kontribusi + keputusan eksperimen |

Pemilik menangani pembicaraan, verifikasi penyedia, kesepakatan fee, komitmen order, pembayaran dan keluhan. Agent membantu meriset, membandingkan, menghitung, menulis, dan mengingatkan pekerjaan. Setelah bottleneck nyata diketahui, baru tambahkan integrasi untuk pekerjaan yang berulang.

## Data

`brief.json`: konteks bisnis; ubah kota setelah dipilih, bukan menjadi fakta pasar otomatis.
`data/leads.csv`: calon pembeli/klien, sumber, status kontak dan penolakan.
`data/suppliers.csv`: kandidat penyedia, quote, kapasitas, syarat dan status verifikasi.
`data/deals.csv`: nilai order, fee, status transaksi serta pemenuhan.
`data/events.csv`: riwayat kejadian bertanggal agar perubahan status tidak menghapus histori.
`data/experiments.csv`: denominator outreach, percakapan, proposal, pembayaran, biaya dan jam pemilik.

Header kosong disengaja. Tidak ada leads atau pesanan rekaan. CSV bukan aplikasi CRM; hindari perubahan paralel pada file yang sama. Sebelum mengisi data nyata, pindahkan data operasional ke penyimpanan privat/CRM dengan akses terbatas. `ops/data/*.csv` di repositori ini adalah template publik: jangan commit data pribadi, catatan pelanggan, invoice atau detail order ke GitHub. Simpan salinan kerja di luar checkout atau jalur privat yang diabaikan Git. `ops/runs/` diabaikan Git karena laporan dapat memuat data operasional.

Baca STRATEGI.md untuk hipotesis dan kriteria berhenti. Jangan mengubah harga atau situs publik hanya karena agent merekomendasikannya.

## Pengujian runner

```sh
python3 -m unittest discover -s ops -p test_agent.py -v
```

Lima tes lokal memeriksa penerusan tugas via stdin tanpa shell, sandbox read-only, laporan sukses, kegagalan CLI, laporan hilang, dan timeout. Tes memakai mock proses model, bukan bukti autentikasi atau integrasi kanal pemasaran.

## Jalur pilihan pemilik: chat Codex

Mulai dari [CHAT-START.md](CHAT-START.md). Runner terminal kini sudah dicoba: endpoint model ditolak proxy CONNECT 403 dan percobaan dihentikan. Gunakan agent dalam chat untuk pekerjaan saat ini; bukan meminta kredensial baru.

## Hasil run chat terbaru

Dua agent telah selesai: [penilaian model bisnis](runs/chat-market-assessment.md) dan [scout Surabaya](runs/chat-surabaya-scout.md). Rekomendasi terbaru adalah menguji meja penawaran catering B2B sebelum broker coffee break, karena pendiri belum memiliki jaringan pembeli/penyedia. Ini hipotesis keputusan, bukan riset pasar terverifikasi atau perubahan harga publik. Tidak ada leads yang dibuat dari ingatan dan tidak ada pesan dikirim.

## Product Hunter — fokus barang jualan

Untuk kebutuhan terbaru pemilik (FMCG, modal Rp1 juta), gunakan `$product-hunter` dan [PRODUCT-HUNTER.md](PRODUCT-HUNTER.md). Agent ini memakai `product-brief.json` tersendiri sehingga tidak membawa harga atau strategi jasa campaign ke riset produk. Runner mendukung role `product-hunter`; enam tes lokal lulus termasuk pemisahan konteks tersebut. Bukti supplier/market tetap memerlukan akses sumber nyata.
