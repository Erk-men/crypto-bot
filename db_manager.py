import sqlite3
from datetime import datetime

# Veritabanı dosyamızın adı
DB_NAME = "crypto_history.db"

def init_db():
    """Veritabanını ve tabloyu oluşturur (Eğer yoksa)"""
    # 1. Bağlantıyı aç
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 2. Tabloyu oluştur (SQL Sorgusu)
    # Tablo adı: prices
    # Sütunlar: id (Otomatik sayı), price (Ondalıklı sayı), date (Yazı)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price REAL,
            date TEXT
        )
    ''')
    
    # 3. Değişiklikleri kaydet ve kapat
    conn.commit()
    conn.close()
    print("Veritabanı ve tablo hazır! ✅")

def add_price(price):
    """Gelen fiyatı veritabanına kaydeder"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Şu anki zamanı alalım (Yıl-Ay-Gün Saat:Dakika:Saniye)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 4. Veriyi ekle (SQL Sorgusu)
    # Soru işaretleri (?) güvenlik içindir (SQL Injection önlemi)
    cursor.execute("INSERT INTO prices (price, date) VALUES (?, ?)", (price, current_time))
    
    conn.commit()
    conn.close()
    print(f"Veri kaydedildi: {price}$ - {current_time}")

# Bu dosya doğrudan çalıştırılırsa tabloyu oluştursun (Test için)
if __name__ == "__main__":
    init_db()