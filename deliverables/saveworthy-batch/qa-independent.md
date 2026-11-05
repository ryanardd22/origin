# Independent sampled QA — tiga video edukasi AI

Reviewed 2026-11-05. **Ketiga video: PASS untuk cerita, visual sampel dan format teknis artifact final yang tercantum di bawah. Tidak ada blocker tersisa pada sampel yang diperiksa.** Belum ada pendengaran manusia atau continuous playback dalam review ini; ini bukan PASS audiovisual tanpa batas.

## Artifact dan status

| File | Durasi / frame | SHA-256 yang diperiksa | Status |
| --- | --- | --- | --- |
| cek-jawaban-ai.mp4 | 50.566667s / 1517 | `30151af6e4395666c47294608f24a5d9b97e0d6fd87764709d0a04a7ee03a173` | PASS sampel |
| revisi-satu-bagian.mp4 | 51.066667s / 1532 | `f63caf40237af87787008b18fff0cc535fc983f84057317ba1689685e56caa6f` | PASS sampel |
| catatan-jadi-tugas.mp4 | 52.600000s / 1578 | `fab4924809c9b12a8a4cd82c276b206898e093b6c2cac74ceea64f001dcb6420` | PASS sampel setelah perbaikan |

Reviewer menghitung hash di atas dan menjalankan ffprobe pada ketiga MP4 deliverables: semuanya 720×1280, 30fps, H.264/yuv420p, AAC stereo 48kHz. Laporan editor mencatat full decode lulus dan tidak ada black events; reviewer membaca bukti tersebut tanpa mengulangi full decode.

## Bukti visual aktual

Ketiga `out/qa/contact.jpg` dilihat, mencakup semua chapter, satu pasangan batas adegan dan sampel dekat akhir masing-masing video. Gambar penuh `frame-10.jpg` untuk check/revision dan `frame-09.jpg` untuk meeting diperiksa. Meeting memiliki frame-00 sampai 09, bukan frame-10. Sampel dekat akhir bukan frame terakhir persis, sehingga reviewer juga mengekstrak sendiri dan melihat frame terakhir 1516 dari check dan 1531 dari revision. Frame 980 check dan 880 revision diekstrak langsung dari MP4 untuk memeriksa stamp setelah fade serta perbandingan lengkap. Setelah export meeting diperbaiki, reviewer memeriksa `frame-07.jpg` yang dibuat ulang dan mengekstrak sendiri frame 521 serta frame terakhir 1577 dari MP4 pengganti. ffprobe dan SHA-256 MP4 pengganti diverifikasi ulang sendiri: 52.600000s, 1578 frame, 4,291,351 byte.

- **Cek Jawaban AI:** tiga pemeriksaan sumber, dukungan isi dan konteks tersampaikan jelas. Klaim “Semua pekerjaan bisa otomatis” diberi label contoh dan ditandai belum terverifikasi; bukan janji otomasi. Kesamaan jawaban dua AI secara eksplisit disebut bukan bukti dan bukan demo model. Stamp pada sampel frame 954 masih masuk fade; frame 980 menunjukkan BELUM TERVERIFIKASI dengan kontras penuh. Checklist terakhir terbaca dan menyatakan tiga cek bukan jaminan benar. Tangan host sempat mendekati awal catatan kecil di bawah checklist, tetapi pada frame terakhir catatan utuh dan seluruh isi penting tetap terbaca. Tidak ada blocker.
- **Revisi Satu Bagian:** before/after lengkap pada frame 880 terbaca; pembuka diringkas dan contoh/penutup ditampilkan sebagai dipertahankan. Label ILUSTRASI TEKS · BUKAN REKAMAN MODEL menghindari klaim palsu bahwa output model telah diuji. Adegan drift menunjukkan bagian lain dapat berubah, diikuti pemeriksaan. Checklist akhir berisi bagian/perubahan/yang dipertahankan dan terbaca utuh. Host dekoratif kecil sedikit melewati sisi kiri, tetapi wajah, gestur, teks utama dan checklist tidak mengalami crop bermakna. Tidak ada blocker.
- **Catatan Jadi Tugas, final setelah perbaikan:** tabel empat kolom, tenggat/status belum disebutkan, keputusan promo tertunda dan catatan Jumat perlu konfirmasi jelas. Masalah sebelumnya pada baris Bima yang melewati tepi kartu sudah selesai: frame aktual 521 dan `frame-07.jpg` yang dibuat ulang menampilkan “Bima mengecek” / “stok.” dalam dua baris dengan margin yang memadai. Reviewer juga melihat master perbaikannya dan source line break. Blank template akhir pada frame 1577, judul, empat header dan instruksi konfirmasi ke orangnya terbaca. Tidak ada blocker.

Tidak ditemukan blank frame atau kegagalan anatomi/occlusion yang menghalangi pemahaman pada sampel ketiga video yang lulus. Heading yang masih fade pada sampel batas adegan bukan layar kosong; karakter dan komposisi tetap terlihat. Penilaian ini terbatas pada sampel, bukan seluruh rangkaian gerak.

## Naskah, template, caption dan subtitle

Ketiga `production/narration-parts.json`, berkas narasi delivery, template TXT dan caption TXT dibaca. Semuanya memberikan langkah praktis yang dapat disalin, tanpa pendapatan, jaminan engagement atau hasil pelanggan rekaan. Template check mengharuskan sumber dibuka sendiri dan kredibilitas tetap dinilai. Template meeting hanya mengambil tindakan yang disebut, tidak mengarang orang/tanggal/status, serta memisahkan keputusan tertunda dan meminta konfirmasi. Template revision meminta batas perubahan serta membandingkan fakta dan bagian yang harus dipertahankan, tanpa menjamin kepatuhan model sempurna. Caption konsisten dengan isi video dan tidak mengklaim sudah diposting.

SRT ketiganya diperiksa intervalnya: 38 / 43 / 42 cue, tidak ada overlap; waktu akhir 48.500 / 50.500 / 49.033 detik, semuanya sebelum durasi masing-masing video. Ini pemeriksaan teks/timing, bukan penilaian sinkronisasi audibel.

## Audio dan batas review

Reviewer membaca `out/qa/asr.json` ketiga proyek: transkripsi otomatis berasal dari final mixed MP4 audio dan mencakup urutan utama narasi masing-masing. Ada recognition berbeda seperti “Jawaverse”, “cetatan”, “rinkas” atau “Bake”; itu tidak cukup untuk memastikan kesalahan pelafalan ataupun menyatakan pelafalan sempurna. ASR meeting dijalankan ulang pada export pengganti: reviewer membaca 20 segmen dan transkrip yang mencakup narasi utama. `mp4_sha256` dalam ASR cocok dengan hash final meeting yang dihitung reviewer, dan `audio_sha256` tercatat `16f7c71fd9d1f8c23994953d524ba3b205cce4f990578235941f8f28e3c09cb7`. Ini identitas bukti otomatis, bukan pendengaran manusia.

Laporan teknis editor mencatat integrated loudness check/meeting/revision sekitar -16.0 / -15.9 / -16.2 LUFS dan true peak -2.6 / -1.8 / -2.6 dBFS. Ini pengukuran, bukan pendengaran reviewer. Intelligibility subjektif, balance musik, ekspresi suara dan smoothness kontinu belum dinilai. Tidak ada upload, posting sosial, source/render/audio mutation oleh reviewer; perubahan hanya laporan ini dan ekstraksi QA sementara di `/tmp`.
