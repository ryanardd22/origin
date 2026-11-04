# QA independen — tes gerak stickman

Verdict: **PASS untuk bukti gerak tubuh dan visual sampel tes 5 detik.** Tidak ditemukan blocker pada sampel yang diperiksa. Ini bukan klaim telah menonton playback kontinu atau mendengarkan audio.

Artifact: `out/stickman-motion.mp4` (267,849 byte), SHA-256 `08f82fbb7c15e92cd96009a9487ccb19a0f7570947bc8c9ed617bdb9ed19f522`.

Pemeriksaan: membaca `src/Video.tsx`; melihat contact 12 frame `out/qa-final.jpg` dan gambar penuh `out/qa-writing-v2.jpg`; menjalankan ffprobe sendiri; mengekstrak dan melihat frame 0, 45, 65, 85, 105, 130, 149 langsung dari MP4 final. Frame terakhir juga dibuka ukuran penuh. Tidak mengubah source/render dan tidak memakai API eksternal.

- Metadata aktual: 5.000s, 150 frame, 30fps, 720×1280, H.264/yuv420p, AAC stereo 48kHz.
- Kamera, meja, judul dan latar tetap. Tubuh berpindah dari kiri menuju meja; kaki menekuk/berganti posisi dan lengan berubah sudut. Source menggerakkan sendi melalui inverse kinematics. Ini animasi artikulasi stickman, bukan gerak zoom/pan foto.
- Frame 65 menunjukkan tangan menjangkau alat di meja. Pada frame 85, tablet sudah terangkat dan berubah orientasi; celah jelas terlihat antara tablet dan meja. Tangan kiri mengikuti sisi tablet.
- Frame 105/130/149 menunjukkan posisi tangan/pena berbeda dan guratan muncul bertahap. Ujung pena dihitung mengikuti koordinat penulisan. Bagian guratan bawah tertutup lengan di akhir, tetapi gerak menulis dan hasil guratan atas tetap terbaca; bukan blocker tes gerak ini.
- Perbandingan frame awal/akhir memperlihatkan perubahan pose dan properti yang nyata. Tidak ditemukan frame kosong, crop anggota tubuh/tablet, atau anatomi stickman yang memblokir pemahaman aksi pada sampel.
- Judul dan indikator BERJALAN → AMBIL → TULIS tetap di dalam frame dan indikator aktif mengikuti fase aksi.

Batas: kelancaran gerak kontinu dan sinkronisasi/kenyamanan audio belum dinilai lewat playback atau pendengaran. Review ini tidak mempublikasikan file; status unggahan GitHub/GIF menjadi tanggung jawab langkah delivery utama. Klaim hasil sebaiknya “tes animasi stickman 5 detik dengan gerak sendi”, bukan animasi karakter realistis.
