import time
import statistics
import speedtest
from selenium import webdriver
from tqdm import tqdm

# İnternet hızını ölçen fonksiyon
def measure_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Mbps
    upload_speed = st.upload() / 1_000_000  # Mbps
    return download_speed, upload_speed

# Web sayfasının yükleme süresini ölçen fonksiyon
def measure_load_time(url, driver):
    start_time = time.time()
    driver.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

# İnternet hızını ölç ve yazdır
print("İnternet hızı ölçülüyor...")
download_speed, upload_speed = measure_internet_speed()
print(f"İnternet hızı: {download_speed:.2f} Mbps indirme, {upload_speed:.2f} Mbps yükleme")

# Tarayıcıyı başlat
driver = webdriver.Chrome()

# Test edilecek web sayfası
url = input("Test etmek istediğiniz URL'yi girin: ")

# Yükleme sürelerini ölçme sayısı
num_measurements = 5

# Web sayfasının yükleme sürelerini ölç, istatistikleri hesapla ve yazdır
load_times = []
for _ in tqdm(range(num_measurements), desc="Yükleme süreleri ölçülüyor"):
    load_time = measure_load_time(url, driver)
    load_times.append(load_time)

avg_load_time = statistics.mean(load_times)
std_dev_load_time = statistics.stdev(load_times)
median_load_time = statistics.median(load_times)

print(f"{url} için yükleme süreleri istatistikleri:")
print(f"  Ortalama: {avg_load_time:.2f} saniye")
print(f"  Standart sapma: {std_dev_load_time:.2f} saniye")
print(f"  Medyan: {median_load_time:.2f} saniye")

# Tarayıcıyı kapat
driver.quit()
