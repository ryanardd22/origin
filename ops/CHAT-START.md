# Jalankan lewat chat Codex

Pilihan pemilik: chat Codex dulu. Tidak perlu dashboard, server bot, atau API key baru untuk menjalankan peran dalam sesi chat yang mendukung agent.

## Cara akses

Buka proyek/repositori `origin` di Codex yang memuat berkas paket ini. Jika paket masih lokal dan belum ada di GitHub, gunakan workspace percakapan ini atau impor paket terlebih dahulu; menghubungkan GitHub tidak otomatis mengunggah perubahan lokal.

Instruksi siap pakai:

> Baca `.agents/skills/origin-growth/SKILL.md` dan `ops/CHAT-START.md`. Jalankan agent scout dan analyst untuk uji meja penawaran catering B2B Surabaya. Gunakan konteks dan CSV aktual. Tulis hasil ke `ops/runs/` dengan nama unik. Tampilkan ringkasan keputusan dan tiga pekerjaan berikutnya di chat. Pisahkan fakta, asumsi, dan bukti yang belum ada. Jangan menghubungi calon pelanggan atau mengubah harga publik.

Jika fitur delegasi tidak tersedia pada sesi, jalankan peran berurutan dalam chat dan beri label hasil tiap peran. Jangan menyebutnya proses paralel jika tidak benar-benar didelegasikan. Menyebut nama skill atau berkas bukan bukti agent berjalan: hasil harus ada dan dapat dibaca.

## Status akses yang diuji

- Agent dalam chat: dijalankan dalam sesi ini untuk evaluasi model bisnis dan scout Surabaya; dua laporan selesai di ops/runs/chat-market-assessment.md dan ops/runs/chat-surabaya-scout.md.
- Runner terminal: dicoba pada sesi ini, namun endpoint model chatgpt.com/backend-api/codex/responses ditolak proxy CONNECT 403. Percobaan ulang dihentikan. Tidak ada laporan analisis model yang dihasilkan oleh jalur CLI pada percobaan tersebut.
- Ini bukan kegagalan kode bisnis atau bukti akun belum login. Jangan meminta token baru atau menonaktifkan TLS untuk memperbaikinya.
- Tidak ada scheduler, pengiriman WhatsApp/Instagram/email otomatis, atau proses agent 24 jam.
- Mengaktifkan ulang jalur terminal tidak diperlukan untuk workflow chat. Jika kelak diperlukan, konfigurasi akses endpoint model harus diselesaikan melalui environment settings lalu diuji ulang.

## Siklus harian yang masuk akal

1. Agent membaca bukti baru: quote, respons, kebutuhan acara, biaya dan jam pengerjaan.
2. Agent membuat shortlist dan draft pekerjaan. Tanpa bukti baru, hasilnya daftar hal yang belum diketahui; jangan mengulang riset yang sama untuk terlihat aktif.
3. Pemilik melakukan percakapan dan konfirmasi, lalu mencatat hasil seperlunya di penyimpanan privat.
4. Analyst merangkum apa yang berubah, kendala utama, dan pekerjaan berikutnya.

Tidak perlu enam agent untuk setiap tugas. Dua peran aktif cukup untuk eksplorasi awal. Offer/coordinator dipanggil ketika kebutuhan dan quote nyata sudah ada.
