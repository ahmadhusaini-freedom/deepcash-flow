# 🤖 DeepCashFlow — Autopilot AI Content System

Sistem otomatis yang membuat dan memposting konten edukasi finansial ke YouTube, Instagram, dan TikTok setiap hari pukul 06.00 WIB — tanpa intervensi manual.

## Cara Kerja

```
DeepSeek API          Claude API           ImageMagick
(Trending Topic)  →   (Buat Naskah)   →   (Buat Thumbnail)
                                                  ↓
                           YouTube ← ← ← Poster Agent → → Instagram
                                                  ↓
                                              TikTok
                                                  ↓
                                         Google Sheets Log
```

## Setup

Lihat panduan lengkap di README_SETUP.md atau ikuti langkah di bawah:

1. Clone repo ini
2. Dapatkan semua API key (lihat panduan di folder `setup/`)
3. Tambahkan secrets ke GitHub (Settings → Secrets → Actions)
4. Jalankan workflow manual dari tab Actions untuk tes pertama

## Secrets yang Dibutuhkan

| Secret | Dari |
|--------|------|
| `CLAUDE_API_KEY` | console.anthropic.com |
| `DEEPSEEK_API_KEY` | platform.deepseek.com |
| `YOUTUBE_CLIENT_ID` | Google Cloud Console |
| `YOUTUBE_CLIENT_SECRET` | Google Cloud Console |
| `YOUTUBE_REFRESH_TOKEN` | `python setup/get_youtube_token.py` |
| `IG_ACCESS_TOKEN` | Facebook Graph API Explorer |
| `IG_USER_ID` | Facebook Graph API Explorer |
| `GOOGLE_SHEETS_CREDENTIALS` | Google Cloud → Service Account → JSON |
| `TIKTOK_COOKIE` | Browser (opsional) |

## Struktur Folder

```
deepcash-flow/
├── .github/workflows/daily_autopilot.yml
├── agents/
│   ├── deepseek_trend.py   # Cari trending topic
│   ├── claude_writer.py    # Buat naskah dengan Claude
│   ├── media_factory.py    # Buat thumbnail
│   └── poster.py           # Post ke semua platform
├── utils/
│   ├── sheets_logger.py    # Log ke Google Sheets
│   └── youtube_auth.py     # Helper YouTube OAuth
├── config/settings.py      # Semua konfigurasi
├── setup/                  # Script setup credential
├── main.py                 # Entry point
└── requirements.txt
```

## Lisensi

MIT — bebas digunakan dan dimodifikasi.
