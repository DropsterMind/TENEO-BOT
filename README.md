  <h1>TENEO-BOT by DropsterMind</h1>

  <h2 class="emoji">🧩 Persiapan Awal Jika Menggunakan Windows</h2>
  <h3>1. ✅ Install Python</h3>
  <ul>
    <li>Install Python 3.10 atau lebih baru dari <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></li>
    <li>Pastikan saat install, centang opsi "Add Python to PATH"</li>
  </ul>

  <h3>2. ✅ Cek pip</h3>
  <pre><code>python --version
pip3 --version</code></pre>
  <p>Jika pip tidak terdeteksi:</p>
  <pre><code>python3 -m ensurepip --upgrade</code></pre>

  <h2 class="emoji">🚀 Instalasi Bot VPS</h2>
  <h3>3. ✅ Clone Bot</h3>
  <pre><code>git clone https://github.com/DropsterMind/TENEO-BOT.git
cd TENEO-BOT</code></pre>
  <p>Atau download ZIP dari GitHub dan ekstrak jika menggunakan Windows.</p>

  <h3>4. ✅ Install Dependencies</h3>
  <pre><code>pip3 install -r requirements.txt</code></pre>
  <p>Jika di Termux (Android):</p>
  <pre><code>pkg install python
pip install -r requirements.txt</code></pre>

  <h2 class="emoji">🧾 Konfigurasi Bot</h2>
  <h3>5. ✅ Buat File <code>nano tokens.json</code></h3>
  <p>Isi file seperti ini:</p>
  <pre><code>[
  {
    "Email": "emailkamu@gmail.com",
    "accessToken": "isi_access_token_di_sini"
  }
]</code></pre>

  <h3>6. (Opsional) Buat <code>proxy.txt</code></h3>
  <pre><code>http://127.0.0.1:8080
socks5://127.0.0.1:9050</code></pre>

  <h2 class="emoji">🔄 Jalankan Bot</h2>
  <h3>7. ✅ Jalankan</h3>
  <pre><code>python3 bot.py</code></pre>
  <p>Bot akan menampilkan menu pilihan proxy:</p>
  <pre><code>[1] Use Free Proxy
[2] Use Private Proxy
[3] No Proxy (Direct)</code></pre>

  <h2 class="emoji">📊 Output & Logging</h2>
  <p>Log disimpan otomatis ke file harian: <code>logs_YYYY-MM-DD.txt</code></p>
  <p>Contoh tampilan log:</p>
  <pre><code>✅ [🕒 29/07/25 08:13:48 WIB] [emailmu@gmail.com] Connected 🌐 without proxy
🏆 [🕒 29/07/25 08:13:49 WIB] [emailmu@gmail.com] Points: 5 🎯 | Total: 110 💰 | HB: 20224 ❤️</code></pre>

  <h2 class="emoji">🔁 Fitur Bot</h2>
  <table>
    <tr>
      <th>Fitur</th>
      <th>Penjelasan</th>
    </tr>
    <tr>
      <td>⏱️ Auto Ping</td>
      <td>Setiap 15 detik</td>
    </tr>
    <tr>
      <td>🧠 Smart ID Check</td>
      <td>Daftar Machine ID otomatis jika belum ada</td>
    </tr>
    <tr>
      <td>🔄 Proxy Rotasi</td>
      <td>Dukungan HTTP/HTTPS/SOCKS5</td>
    </tr>
    <tr>
      <td>📦 Logging Harian</td>
      <td>Log rapi harian otomatis dengan emoji</td>
    </tr>
  </table>

  <h2 class="emoji">💬 Bantuan</h2>
  <ul>
    <li>Telegram: <a href="https://t.me/dropstermind" target="_blank">dropstermind</a></li>
  </ul>

  <h2 class="emoji">🖥️ Tips Lanjutan</h2>
  <ul>
    <li>Ingin bot jalan 24 jam? Gunakan VPS</li>
    <li>Jika pakai Linux atau Termux, gunakan <code>screen</code> atau <code>tmux</code></li>
  </ul>

</body>
</html>
