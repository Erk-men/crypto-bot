import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Veritabanı adı (main.py'deki ile aynı olmalı)
DB_NAME = "crypto_history.db"

def plot_bitcoin_history():
    print("Veriler analiz ediliyor... ")
    
    # 1. Veritabanına Bağlan
    conn = sqlite3.connect(DB_NAME)
    
    # 2. SQL ile veriyi çek ve Pandas DataFrame'e yükle (Tek satırda profesyonel yöntem)
    df = pd.read_sql_query("SELECT * FROM prices", conn)
    
    conn.close()
    
    # Veri var mı kontrol et
    if df.empty:
        print("Veritabanı boş! Botu biraz çalıştırıp veri toplamasını bekle.")
        return

    # 3. 'date' sütununu gerçek tarih formatına çevir
    df['date'] = pd.to_datetime(df['date'])
    
    # 4. Grafiği Çiz
    plt.figure(figsize=(10, 5)) # Pencere boyutu
    plt.plot(df['date'], df['price'], marker='o', linestyle='-', color='b', label='BTC Price')
    
    # Süslemeler
    plt.title('Bitcoin Fiyat Geçmişi')
    plt.xlabel('Tarih / Saat')
    plt.ylabel('Fiyat ($)')
    plt.grid(True) # Izgara çizgileri ekle
    plt.legend()
    
    # X eksenindeki tarihleri okunabilir yap (Eğik yazdır)
    plt.xticks(rotation=45)
    plt.tight_layout() # Sıkışıklığı önle
    
    # 5. Göster!
    print("Grafik oluşturuldu! Pencere açılıyor... ")
    plt.show()

if __name__ == "__main__":
    plot_bitcoin_history()