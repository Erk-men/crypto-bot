import os
import asyncio  # <-- Yeni kütüphanemiz
import aiohttp  # <-- Requests yerine geçen asenkron kütüphane
import logging
import sys
from plyer import notification
from dotenv import load_dotenv
from db_manager import init_db, add_price
from analyzer import calculate_sma

# Ayarları Yükle
load_dotenv()
CRYPTO_ID = os.getenv("CRYPTO_ID", "bitcoin")
CURRENCY = os.getenv("TARGET_CURRENCY", "usd")
TARGET_PRICE = float(os.getenv("TARGET_PRICE", 100000))
INTERVAL = int(os.getenv("CHECK_INTERVAL", 10))

# Logging Ayarları
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot_logları.log"),
        logging.StreamHandler()
    ]
)

# async: Bu fonksiyonun asenkron çalışacağını belirtir
async def get_crypto_price(session):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO_ID}&vs_currencies={CURRENCY}"
    try:
        # await: Cevap gelene kadar bekle ama o sırada başka iş varsa yap (bloklama)
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json() # JSON çevirme de asenkrondur
                return data[CRYPTO_ID][CURRENCY]
            elif response.status == 429:
                logging.warning(" Rate Limit! Biraz bekliyoruz...")
                return None
            else:
                logging.error(f"Hata Kodu: {response.status}")
                return None
    except Exception as e:
        logging.error(f"Bağlantı Hatası: {e}")
        return None

async def main():
    logging.info("---  ASENKRON KRİPTO BOTU BAŞLATILDI (v2.0) ---")
    init_db()
    
    # Asenkron bir 'Session' (Oturum) açıyoruz. Sürekli aç-kapa yapmaktan daha hızlıdır.
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                price = await get_crypto_price(session)
                
                if price:
                    # Not: DB işlemleri genelde senkrondur ama çok hızlı olduğu için
                    # burada await kullanmadan çağırabiliriz.
                    add_price(price)
                    
                    # Analiz Yap
                    sma_value = calculate_sma(window=5)
                    trend_msg = ""
                    if sma_value:
                        if price < sma_value:
                            trend_msg = f" (Trend: DÜŞÜŞ - Ort: {sma_value:.2f})"
                        else:
                            trend_msg = f" (Trend: YÜKSELİŞ - Ort: {sma_value:.2f})"
                    
                    logging.info(f"Fiyat: {price} {CURRENCY} {trend_msg}")
                    
                    # Alarm Kontrol
                    if price < TARGET_PRICE:
                        logging.warning(f" ALARM! {price}")
                        notification.notify(
                            title=f"DİKKAT! {CRYPTO_ID} DÜŞTÜ!",
                            message=f"Fiyat: {price} {CURRENCY}",
                            timeout=5
                        )
                
                # EN ÖNEMLİ KISIM: Programı dondurmadan bekle
                await asyncio.sleep(INTERVAL)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                logging.critical(f"Kritik Hata: {e}")
                await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    # Asenkron döngüyü başlat
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot durduruldu. Görüşmek üzere! ")