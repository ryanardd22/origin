# QA independen — kartun penjelasan AI

Verdict final V2: **PASS untuk cerita, visual sampel, dan format teknis file final.** Tidak ditemukan blocker yang menghalangi pemahaman cerita pada bukti yang diperiksa. Audio memiliki bukti transkripsi otomatis yang berhasil, tetapi **belum dinilai lewat pendengaran manusia**. Ini bukan kelulusan audiovisual tanpa batas.

Artifact final V2: `out/ai-explainer.mp4`, 6,802,605 byte.
SHA-256: `620fb501c3471fc4eb035cbb6f0f68a332e18176660e44b2a372abd77dd6aecc`.

## Pemeriksaan yang dilakukan

- Membaca `voiceover.txt`, 8 bagian `production/narration-parts.json`, `production/edit-timeline.json`, `public/edit-data.json`, `src/Video.tsx`, `src/Art.tsx`, `production/audio-asr-check.json`, dan `out/qa/technical-report.json`. Timeline produksi dan data yang diimpor source identik. Naskah dan caption masing-masing memiliki 131 kata.
- Review awal sebelum patch: melihat tiga contact yang mencakup 23 frame semua 8 chapter. Membuka key 05, 06, 09, 13, 14, 15, 16, 21 dan 23 ukuran penuh untuk caption, gestur, permintaan lucu, workflow, sumber/bantuan agent, gabungan aplikasi dan penutup.
- Review awal sebelum patch: melihat semua 14 boundary yang disediakan dalam contact sementara. Mengekstrak sendiri dan melihat frame 0, 486, 1295, 1585 dan 1739 langsung dari MP4 sebelum patch untuk memastikan awal, perubahan chat, bantuan agent, gabungan aplikasi dan akhir.
- Pemeriksaan patch V2: melihat frame aktual `out/qa/patch-1280.jpg`, `patch-1295.jpg`, `patch-1326.jpg`; mengekstrak sendiri dan melihat frame 1295 dan 1327 dari MP4 V2. Label sekunder hilang saat bantuan, pertanyaan dan sumber tetap jelas, transisi ke recap tidak blank. Source `ToolRow` mengubah opacity label menjadi 0 sejak cue bantuan. Hash file V2 di atas dihitung ulang sendiri.
- ffprobe independen setelah patch: 58.000s, 1740 frame, 720×1280, 30fps, H.264/yuv420p, AAC stereo 48kHz. Full decode lulus lagi setelah patch tercatat dalam laporan teknis editor utama; reviewer tidak mengulangi full decode atau menonton continuous playback. Laporan teknis juga mencatat hash PCM audio sebelum/sesudah sama (`90f8644ccac3f60f4edf3dd347934e6f82f38e160bdbae5f9644f8f4f0e5c99f`); ini bukti editor bahwa audio tidak berubah, bukan pendengaran reviewer.

## Cerita dan akurasi

Satu kasus “menyiapkan konten teknologi” dipertahankan dari tujuan awal hingga chat, workflow, agent dan rangkuman. Chat memperlihatkan permintaan ide, tanggapan, permintaan versi lebih lucu, lalu ide baru. Workflow menampilkan urutan TOPIK → NASKAH → DOKUMEN dengan aktivasi langkah dan kertas mengikuti kurva yang sama dengan jalur source. Agent memiliki tujuan, alat terhubung, pencarian, pembacaan sumber, pencarian ulang saat bahan kurang, dan pertanyaan ketika memerlukan bantuan.

Framing “tiga cara pakai AI” merupakan penyederhanaan yang layak untuk pemula. Penutup secara eksplisit menyatakan ketiganya bukan kotak terpisah dan satu aplikasi dapat menggabungkannya; source tidak mengklaim seluruh AI hanya terdiri dari tiga jenis. Dialog chat dapat menjadi antarmuka untuk sistem gabungan. Kemampuan memilih alat dikondisikan pada alat yang terhubung, bukan jaminan semua chatbot memiliki akses alat. “Panduan resmi” dan “Penjelasan teknis” adalah label ilustrasi, bukan klaim sumber nyata yang telah dicari dalam video ini.

Cue permintaan lucu berada pada kalimat “coba yang lebih lucu”; konfirmasi ide pada “idenya pas”. Aktivasi workflow sesuai urutan yang dinarasikan. Sumber, panah pencarian ulang dan pertanyaan bantuan muncul pada bagian kalimat terkait. Ini pemeriksaan source/timestamp serta frame, bukan penilaian sinkronisasi dengan pendengaran.

## Visual

Heading dan caption memiliki kontras baik, tetap di dalam canvas, dan terbaca pada sampel penuh. Caption panjang seperti “Kalau alatnya terhubung,” dan “menggabungkan semuanya.” tetap memiliki margin. Teks utama kartu tujuan, sumber, jawaban chat dan gabungan aplikasi tetap dapat dipahami. Tidak ditemukan crop anggota tubuh, kerusakan anatomi kartun yang memblokir aksi, atau layar kosong pada frame/boundary yang diperiksa. Judul masuk dengan fade singkat pada batas chapter, sementara karakter dan ruang tetap terlihat.

Perubahan pose lengan/tangan, arah perhatian dan pergerakan properti terlihat antar cue. Lensa tetap mengikuti tangan melalui koordinat yang sama. Mulut dipengaruhi amplitude narasi; ini bukan lip-sync fonem. Penutup frame 1739 tetap menampilkan pertanyaan dan ketiga pilihan, tanpa caption yang terpotong. Chapter bersambung tanpa gap, caption tidak overlap; caption terakhir berakhir di frame 1701, setelah kata terakhir bertimestamp 56.584s. Durasi narasi yang tercatat 56.72s menyisakan 1.28s sebelum video berakhir.

Temuan label sekunder “ALAT TERHUBUNG” yang tertutup bubble bantuan pada versi awal sudah diperbaiki dalam V2 dengan menyembunyikannya selama bantuan. Frame patch aktual tidak lagi memperlihatkan potongan label. Contact versi awal hanya menjadi bukti cakupan adegan lain, bukan bukti patch. Polish kecil yang tetap bukan blocker: tangan pada jawaban chat mendekati tepi kiri teks “ikut rapat…”, tetapi frasa tetap terbaca pada key 06.

## Batas kesimpulan

ASR lokal `faster-whisper base int8 CPU` berhasil menghasilkan 17 segmen yang mencakup semua bagian utama naskah. Ada perbedaan ejaan/recognition seperti AI→AE, kotak→kota dan ajak→agak; ini tidak membuktikan kesalahan pengucapan dan juga tidak cukup untuk menyatakan pelafalan sempurna. Reviewer tidak mendengar audio. Kenyamanan suara, emosi, keseimbangan musik, smoothness kontinu dan lip-sync perseptual belum dinilai lewat playback.

Hasil ini adalah video penjelasan kartun dengan narasi, bukan rekaman sistem AI sungguhan menjalankan pencarian/alat. Review tidak mengunggah file dan tidak memverifikasi tautan publik. Rencana delivery adalah unduhan GitHub; tidak ada posting sosial oleh reviewer.

Perubahan proyek oleh reviewer hanya laporan ini. Source, render dan audio tidak diubah.
