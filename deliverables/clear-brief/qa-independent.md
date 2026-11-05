# QA independen — AI: tugas yang lebih jelas

Reviewed 2026-11-05. Verdict: **PASS untuk cerita, visual sampel, dan format teknis file final.** Tidak ditemukan blocker pada bukti yang diperiksa. Review ini tidak mencakup pendengaran manusia atau playback kontinu.

Artifact: `out/clear-brief.mp4`, 6,173,363 byte.
SHA-256 independen: `06001a1eedacb4daf38d7105790a1f01f8f0215c811f046d0a15295b15e7e574`.

## Bukti yang diperiksa

- Membaca `voiceover.txt`, `src/Video.tsx`, data `public/edit-data.json`, `production/research-notes.json`, `production/audio-asr-check.json`, `out/qa/final-audio-asr.json`, dan `out/qa/technical-report.json`. SHA-256 `src/Art.tsx` identik dengan versi kartun explainer sebelumnya yang telah direview. Naskah dan caption masing-masing 123 kata.
- Melihat empat contact final yang mencakup 34 keyframes seluruh 8 chapter; membuka key 15, 16, 19 dan 25 ukuran penuh. Semua 14 boundary dilihat melalui contact sementara.
- Mengekstrak sendiri dan melihat frame 0, 818, 840, 1190 dan 1508 langsung dari MP4 final. Pemeriksaan ini menguji hook awal, baris ketiga format, penjelas target 30 detik, label konfirmasi setelah fade, dan penutup.
- ffprobe independen: 50.300s, 1509 frame, 720×1280, 30fps, H.264/yuv420p, AAC stereo 48kHz. Full decode lulus dicatat dalam laporan teknis editor utama; reviewer tidak mengulang full decode. Laporan teknis final juga mencatat integrated loudness -15.8 LUFS, true peak -1.5 dBFS, dan tidak ada interval hitam. Ini pengukuran editor, bukan penilaian pendengaran reviewer.

## Cerita dan batas klaim

Satu permintaan umum “Bantu aku bikin konten” diperjelas lewat pertanyaan tentang audiens, bahan dan bentuk hasil; empat pegangan kemudian dipakai untuk menyusun contoh permintaan yang lebih lengkap. Tugas, konteks audiens pemula, tiga poin bahan, dan bentuk hasil terlihat nyata di kartu contoh. Ketiga poin catatan ditampilkan, bukan hanya disebut sebagai bahan yang tidak pernah terlihat. Bagian revisi berfokus pada pembuka, lalu pemeriksaan fakta dan penandaan informasi yang belum jelas menghindari kesan bahwa instruksi lebih lengkap menjamin jawaban benar.

“Empat pegangan” dan “cara praktis” adalah heuristic yang layak, bukan klaim aturan universal atau taksonomi resmi. Catatan riset menunjuk artikel resmi OpenAI untuk kejelasan, konteks, iterasi dan tone; pembagian tugas/konteks/bahan/format dinyatakan sebagai ringkasan produksi sendiri. Reviewer memeriksa catatan riset yang disediakan, tidak mengambil ulang halaman web. Tidak ada janji pendapatan, hasil pasti, tren atau performa platform.

**Target 30 detik adalah contoh permintaan kepada AI.** Kartu diberi label CONTOH PERMINTAAN, barisnya berbunyi “Target 30 detik.”, dan frame 840 menampilkan penjelas “30 detik = target contoh tugas.” Video final sendiri berdurasi 50.3 detik. Tidak ada klaim hasil contoh video 30 detik telah benar-benar dihasilkan. Ini ilustrasi penyusunan instruksi, bukan demonstrasi output model nyata.

## Visual dan timeline

- Heading, bubble awal, pertanyaan lanjutan, kartu contoh, tiga poin bahan, instruksi revisi dan checklist fakta terbaca pada sampel. Tidak ditemukan crop teks penting, anggota tubuh atau kartu; tangan menunjuk dari tepi tanpa menutup isi utama.
- Empat warna konsisten pada framework, kartu contoh, recap dan outro: tugas mint, konteks ungu, bahan emas, format biru.
- Key 19 / frame 818 menampilkan “Tutup: 1 pertanyaan.” utuh di baris ketiga FORMAT HASIL. Penjelas target contoh di frame 840 lebih kecil daripada isi kartu, tetapi terbaca pada frame penuh, berada di dalam canvas dan tidak terpotong.
- PERLU KONFIRMASI pada key 25 / frame 1155 baru masuk fade. Frame 1190 yang diekstrak sendiri memperlihatkan label emas penuh, kontras baik dan teks utuh; tidak ada masalah kontras menetap.
- Hook frame 0 sudah memuat bubble permintaan, karakter dan tanda tanya saat heading belum masuk. Batas chapter memakai fade heading singkat; tidak ada layar kosong pada sampel. Source memakai artikulasi sendi, gestur, mulut dan properti SVG, bukan foto yang hanya di-zoom.
- Akhir frame 1508 mempertahankan pertanyaan dan empat pegangan yang terbaca. Delapan chapter bersambung tanpa gap; caption tidak overlap. Kata terakhir berakhir 48.870s dan caption terakhir berakhir di frame 1469 (48.967s). Narasi WAV diukur independen 49.041s, menyisakan 1.259s sebelum video berakhir.

## Audio dan keterbatasan

`production/audio-asr-check.json` menyediakan 13 segmen transkripsi otomatis yang mencakup semua bagian utama narasi. Ejaan/recognition seperti “AI kemudian” untuk pembuka dan “cetatan/naska/rinkas” tidak membuktikan kesalahan pengucapan dan juga tidak membuktikan pelafalan sempurna. File ini merupakan pemeriksaan raw voice. Reviewer juga membaca `out/qa/final-audio-asr.json`, transkripsi otomatis audio MP4 final yang memuat 19 segmen dari pembuka sampai pertanyaan penutup. Sepuluh kata kunci (tugas, konteks, bahan, format, konten, pemula, santai, kalimat, fakta, dikonfirmasi) terdeteksi. Ada perbedaan recognition tambahan seperti “Bagaimana” untuk “Bagian mana”; tidak ada bukti bagian utama hilang dari transkripsi ini. Pemeriksaan otomatis tersebut mendukung keberadaan narasi dalam mux final, bukan kelulusan pelafalan atau pendengaran manusia. Hash artifact dalam laporan teknis tetap sama dengan hash yang dihitung reviewer.

Tidak ada audio yang didengarkan reviewer/manusia dalam review ini. Kenyamanan suara, keseimbangan musik, pelafalan, sinkronisasi audibel dan smoothness kontinu belum dinilai lewat playback. Gerak mulut mengikuti amplitude, bukan lip-sync fonem. Sampel visual dan metadata tidak setara kelulusan audiovisual tanpa batas.

Review hanya menyimpan laporan ini dalam proyek; source, render dan audio tidak diubah. Review tidak mengunggah hasil, tidak memverifikasi unduhan GitHub dan tidak memposting ke media sosial.
