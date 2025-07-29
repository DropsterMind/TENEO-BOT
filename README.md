# 🧠 TENEO-BOT by DropsterMind

Bot Python 3 untuk auto connect dan auto ping node Teneo. Cocok untuk menjalankan node 24/7 dan mengoptimalkan reward Teneo Points. 🔁🌐

---

## 🛠️ Fitur Utama

| Fitur               | Deskripsi                                                                 |
|---------------------|---------------------------------------------------------------------------|
| ⏱️ Auto Ping         | Ping otomatis setiap 15 detik                                             |
| 🧠 Smart ID Check    | Mendaftarkan Machine ID jika belum ada                                    |
| 🔐 Auto Login        | Menggunakan `accessToken` dari file `tokens.json`                         |
| 🌍 Proxy Support     | Mendukung proxy pribadi / umum (HTTP, HTTPS, SOCKS5)                      |
| 🔄 Proxy Rotation    | Otomatis rotasi proxy jika lebih dari 1                                   |
| 🧾 Log Harian        | Log otomatis dengan format `[logs_YYYY-MM-DD.txt]`                        |
| 🎨 Tampilan Modern   | ASCII Logo DropsterMind + log berwarna dan emoji                         |
| 📊 Statistik Real-Time | Menampilkan info poin, heartbeat, dan koneksi di terminal                |

---

## 🔧 Cara Instalasi

### 1. Clone Repo

```bash
git clone https://github.com/DropsterMind/TENEO-BOT.git
cd TENEO-BOT
```

### 2. Install Python Modules

```bash
pip install -r requirements.txt #or pip3 install -r requirements.txt
```

Untuk pengguna Termux (Android):

```bash
pkg install python
pip install -r requirements.txt
```

---

## 🔐 Konfigurasi Akun

### 3. Buat File `tokens.json`

```json
[
  {
    "Email": "your_email_address_1",
    "accessToken": "your_access_token_1"
  },
  {
    "Email": "your_email_address_2",
    "accessToken": "your_access_token_2"
  }
]
```

> 📝 *Token bisa didapat dari inspect browser saat login ke dashboard.teneo.pro*

---

### 4. (Opsional) Buat File `proxy.txt`

```
http://127.0.0.1:8080
socks5://127.0.0.1:9050
```

---

## 🚀 Menjalankan Bot

```bash
python setup.py #or python3 bot.py
```

Lalu pilih mode proxy saat diminta:

```
[1] Use Free Proxy
[2] Use Private Proxy
[3] No Proxy (Direct)
```

---

## 🧾 Contoh Log

```log
🟢 [🕒 29/07/25 08:13:46 WIB] 👥 Running 2 accounts without proxy.

✅ [🕒 29/07/25 08:13:48 WIB] [your***email@gmail.com] Connected 🌐 without proxy
🏆 [🕒 29/07/25 08:13:49 WIB] [your***email@gmail.com] Points: 5 🎯 | Total: 105 💰 | HB: 20224 ❤️
```

---

## 🖼️ Tampilan ASCII

```
     _____                             _           _      _           _     
    |  __ \                           | |         | |    (_)         | |    
    | |  | |_ __ ___  _ __   ___  _ __| |_   _ ___| |     _ _ __   __| |___ 
    | |  | | '__/ _ \| '_ \ / _ \| '__| | | | / __| |    | | '_ \ / _` / __|
    | |__| | | | (_) | |_) | (_) | |  | | |_| \__ \ |____| | | | | (_| \__ \
    |_____/|_|  \___/| .__/ \___/|_|  |_|\__,_|___/______|_|_| |_|\__,_|___/
                     | |                                                   
                     |_|                         By DropsterMind
```

---

## ❓ FAQ

- **Token tidak valid?** → Pastikan accessToken masih aktif dari dashboard Teneo.
- **Heartbeat gagal?** → Cek koneksi atau proxy bermasalah.
- **Log kosong?** → Periksa format `tokens.json`.

---

## 🧠 Kontak & Komunitas

- 💬 Telegram: [DropsterMind](https://t.me/dropstermind)

---

## 📌 Tips Tambahan

- Ingin jalan terus 24 jam? Gunakan **VPS** seperti DigitalOcean, Vultr, atau local PC dengan `tmux` / `screen`
- Untuk OS Linux/Termux:
```bash
screen -S teneo
python3 bot.py
```

---

> 🔗 Repo ini: [https://github.com/DropsterMind/TENEO-BOT](https://github.com/DropsterMind/TENEO-BOT)
