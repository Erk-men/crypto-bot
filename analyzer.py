import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

# Ayarları çekelim
load_dotenv()
DB_NAME = os.getenv("DB_NAME", "crypto_history.db")

def calculate_sma(window=5):
    """
    Son 'window' kadar veriyi çeker ve ortalamasını alır.
    Örn: Son 5 fiyatın ortalaması.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        
        # SQL: Son eklenen N tane fiyatı getir (Ters sırala, limiti al)
        query = f"SELECT price FROM prices ORDER BY id DESC LIMIT {window}"
        
        df = pd.read_sql(query, conn)
        conn.close()
        
        # Eğer yeterli veri yoksa (mesela veritabanında sadece 2 kayıt varsa) hesaplama yapma
        if len(df) < window:
            return None
        
        # Ortalamayı hesapla (Pandas'ın gücü)
        average = df['price'].mean()
        return average

    except Exception as e:
        print(f"Analiz Hatası: {e}")
        return None