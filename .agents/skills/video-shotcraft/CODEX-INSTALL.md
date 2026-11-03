# Instalasi Codex untuk Origin

Sumber: https://github.com/Vincentwei1021/video-shotcraft
Commit upstream: 1266a3ec4831289c4d893d42dd5102723658039a

Paket upstream disalin beserta LICENSE, referensi, template dan aset. Tidak memerlukan akun Claude. Skill ditemukan dari `.agents/skills/video-shotcraft/SKILL.md`; sesi baru mungkin diperlukan untuk discovery.

Node/npm, ffmpeg/ffprobe tersedia di environment instalasi. Dependensi template dan root test dipasang memakai npm ci. Render lokal menggunakan Chromium sistem dengan mode chrome-for-testing dan concurrency=1. Proses preview/workbench harus dijalankan ulang pada sesi baru; localhost environment bukan tautan publik untuk HP.

Contoh uji frame (jalankan dari folder template):

```sh
npm ci --no-audit --no-fund
npx remotion still src/index.ts AiflPromo /tmp/shotcraft-check.png --frame=60 --concurrency=1 --chrome-mode=chrome-for-testing --browser-executable=/usr/bin/chromium
```

Validasi aktual: 23 tes helper lulus; PNG 1920×1080 berhasil; potongan template 60 frame berhasil diekspor menjadi MP4 H.264 960×540, 2 detik dengan audio AAC. Ini smoke test instalasi, bukan pengujian seluruh shot atau video produk baru. Paket skill berlisensi Apache-2.0; Remotion dan aset audio memiliki ketentuan terpisah. Rendering lokal tidak menggunakan kredit video GPT/Google. Fitur pencarian suara, publikasi sosial, dan generasi aset dari penyedia lain adalah integrasi terpisah dan belum dikonfigurasi. Tidak ada akun sosial atau API key ditambahkan.
