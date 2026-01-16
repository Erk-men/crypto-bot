# 🚀 Async Crypto Sentinel (Asenkron Kripto Bekçisi)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Asyncio](https://img.shields.io/badge/Architecture-Asyncio-green?style=for-the-badge&logo=fastapi)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge&logo=sqlite)
![Analysis](https://img.shields.io/badge/Data%20Science-Pandas%20%7C%20Matplotlib-orange?style=for-the-badge)

<p align="center">
  <a href="#-english">🇺🇸 English</a> | <a href="#-türkçe">🇹🇷 Türkçe</a>
</p>

---

<div id="-english"></div>

## 🇺🇸 English

### 📖 Overview
**Async Crypto Sentinel** is a high-performance, non-blocking cryptocurrency tracking bot built with Python. Unlike traditional bots, it utilizes **Asynchronous Programming (Asyncio & Aiohttp)** to monitor market prices in real-time without freezing system resources.

It features a built-in **Financial Analysis Engine** that calculates Simple Moving Averages (SMA) to detect trends (Bullish/Bearish) and triggers **Desktop Notifications** when price targets are breached.

### ✨ Key Features
* **⚡ Asynchronous Architecture:** Powered by `asyncio` and `aiohttp` for non-blocking I/O operations.
* **🧠 Intelligent Analysis:** Uses `Pandas` to calculate SMA (Simple Moving Average) and identify market trends.
* **💾 Persistent Memory:** Logs all price movements into a `SQLite` database automatically.
* **🔔 Real-Time Alerts:** Sends cross-platform desktop notifications via `plyer`.
* **📊 Data Visualization:** Generates professional price history charts using `Matplotlib`.
* **📝 Professional Logging:** Features a rotation-ready logging system for debugging and audit trails.

### 🛠️ Tech Stack
* **Core:** Python 3.x, Asyncio
* **Networking:** Aiohttp (Async HTTP Client)
* **Data Science:** Pandas, Matplotlib
* **Database:** SQLite3
* **Utilities:** Plyer (Notifications), Python-Dotenv (Config)

### 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/async-crypto-bot.git](https://github.com/yourusername/async-crypto-bot.git)
    cd async-crypto-bot
    ```

2.  **Create Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration (.env)**
    Create a `.env` file in the root directory and configure your preferences:
    ```ini
    CRYPTO_ID=bitcoin
    TARGET_CURRENCY=usd
    TARGET_PRICE=95000
    CHECK_INTERVAL=10
    ```

### ▶️ Usage
**To start the bot:**
```bash```
python main.py

**To visualize the data (Graph):**
```bash```
python visualize.py

<div id="-türkçe"></div>

###Türkçe
📖 Proje Hakkında
Async Crypto Sentinel, Python ile geliştirilmiş yüksek performanslı bir kripto para takip botudur. Geleneksel botların aksine, Asenkron Programlama (Asyncio & Aiohttp) mimarisini kullanarak sistem kaynaklarını tüketmeden gerçek zamanlı piyasa takibi yapar.

İçerisindeki Finansal Analiz Motoru, Basit Hareketli Ortalamaları (SMA) hesaplayarak piyasa trendini (Yükseliş/Düşüş) tespit eder ve belirlediğiniz fiyatın altına inildiğinde Masaüstü Bildirimi gönderir.

✨ Temel Özellikler
⚡ Asenkron Mimari: asyncio ve aiohttp sayesinde bloklanmayan (non-blocking) veri akışı.

🧠 Akıllı Analiz: Pandas kullanarak geçmiş verileri analiz eder ve trend yönünü belirler.

💾 Veri Madenciliği: Tüm fiyat hareketlerini otomatik olarak SQLite veritabanına kaydeder.

🔔 Anlık Bildirimler: Hedef fiyat kaçtığında plyer ile masaüstü uyarısı gönderir.

📊 Görselleştirme: Toplanan verileri Matplotlib ile profesyonel grafiklere döker.

📝 Profesyonel Loglama: Hata takibi ve geçmiş kayıtları için detaylı .log dosyası tutar.

🛠️ Kullanılan Teknolojiler
Çekirdek: Python 3.x, Asyncio

Ağ: Aiohttp (Asenkron HTTP İstemcisi)

Veri Bilimi: Pandas, Matplotlib

Veritabanı: SQLite3

Araçlar: Plyer (Bildirim), Python-Dotenv (Konfigürasyon)

🚀 Kurulum
Projeyi Klonlayın
git clone [https://github.com/kullaniciadi/async-crypto-bot.git](https://github.com/kullaniciadi/async-crypto-bot.git)
cd async-crypto-bot

Sanal Ortamı Kurun (Önerilen)
# Windows için
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux için
python3 -m venv venv
source venv/bin/activate

Gerekli Kütüphaneleri Yükleyin
pip install -r requirements.txt

Ayarları Yapın (.env) Ana dizinde .env adında bir dosya oluşturun ve şu ayarları kendinize göre düzenleyin:
```ini
    CRYPTO_ID=bitcoin
    TARGET_CURRENCY=usd
    TARGET_PRICE=95000
    CHECK_INTERVAL=10
```
▶️ Kullanım
Botu başlatmak için:
python main.py

Grafik Raporu Almak için:
python visualize.py

📂 Directory Structure (Proje Yapısı)
async-crypto-bot/
├── 📄 main.py           # Entry point & Async Logic (Ana Bot)
├── 📄 analyzer.py       # Data Analysis Module (SMA Calculation)
├── 📄 db_manager.py     # Database Operations (SQLite)
├── 📄 visualize.py      # Data Visualization (Matplotlib)
├── 📄 .env              # Configuration Variables (Gizli Ayarlar)
├── 📄 .gitignore        # Git Exclusions
├── 📄 requirements.txt  # Dependencies
└── 📄 README.md         # Documentation
