# QA independen — prototipe kartun 2D

Verdict: **PASS untuk visual sampel dan format prototipe 12 detik / 3 adegan.** Tidak ditemukan blocker pada bukti yang diperiksa. Ini bukan video penuh naskah, bukan klaim playback kontinu, dan bukan review audio.

Artifact: `out/cartoon-ai-style.mp4` (1,358,382 byte).
SHA-256: `5f01d5042b2137a57345f1738076b507849fedbe883ed20419e433383632a62a`.

Pemeriksaan aktual: membaca `src/Video.tsx`; melihat 9 frame `out/qa-final-contact.jpg` serta gambar penuh `out/qa-final-chat.jpg` dan `out/qa-final-agent.jpg`. Reviewer menjalankan ffprobe sendiri dan mengekstrak frame 0, 119, 120, 239, 240, 359 langsung dari MP4 final untuk memeriksa awal/akhir serta dua batas adegan. Frame 359 dibuka ukuran penuh. Preview `check*` lama tidak dipakai sebagai bukti final. Tidak mengubah source/render dan tidak memakai API eksternal.

- Metadata independen: durasi 12.000s, 360 frame, 30fps, 720×1280, H.264/yuv420p, AAC stereo 48kHz. Main melaporkan full decode lulus; reviewer tidak mengulangi full decode.
- Heading besar, label AI CHATBOT / AI WORKFLOW / AI AGENT, dan ringkasan pada y376 terbaca dengan margin memadai. Ringkasan berada di bawah heading dan tidak bertabrakan dengan karakter. Teks percakapan dan kartu tujuan tetap masuk frame.
- Karakter berwajah, berambut, berpakaian dan berjari memberi detail visual yang lebih kaya daripada stickman. Perubahan posisi lengan/tangan antaradegan dan selama adegan agent terlihat pada sampel; source juga mengubah sendi, tatapan, kedipan, gerak badan dan bot. Tidak menggunakan foto yang hanya di-zoom/pan.
- Lengan/tangan tidak menutup teks utama jawaban chatbot atau “Siapkan bahan konten teknologi.” Kaca pembesar melintasi area label TUJUAN, tetapi isi utama tetap terlihat. Gagang berhubungan dengan posisi tangan dan ikut transform tangan; tidak tampak terlepas pada sampel agent.
- Workflow memiliki urutan TOPIK → NASKAH → SIMPAN. Source menghitung posisi kertas memakai dua segmen kurva Bézier yang sama dengan garis jalur, dengan easing per segmen; contact menunjukkan kertas berpindah di jalur tersebut. Paper/path berada dalam canvas.
- Tidak ditemukan crop anggota tubuh, tangan, sepatu, bot atau teks; tidak ada frame kosong pada sampel. Pada frame 0/120/240, judul sedang opacity0 untuk animasi masuk 12 frame, sedangkan karakter, properti dan ringkasan tetap terlihat. Batas adegan tidak menghasilkan layar kosong.
- Frame 359 mempertahankan heading, kartu tujuan dan instruksi “Cek hasil → pilih lagi” dengan jelas.

Batas delivery: sebut sebagai **prototipe visual kartun 2D 12 detik, 3 adegan, tanpa narasi**. Jangan menyebutnya video naskah lengkap atau demo AI yang benar-benar menjalankan alat; alurnya ilustrasi SVG yang telah diprogram. Audio belum didengarkan dan kelancaran gerak kontinu belum dinilai lewat playback. Review ini tidak melakukan publikasi atau memverifikasi unggahan GitHub/GIF; langkah delivery utama menangani tautan publik tersebut.
