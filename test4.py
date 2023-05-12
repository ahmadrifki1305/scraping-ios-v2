
import threading
import time

# Fungsi untuk loop yang ingin dihentikan dari thread utama
def loop1():
    while True:
        print("Loop 1")
        time.sleep(1)

# Fungsi untuk loop yang akan menghentikan loop1 dari thread utama
def loop2():
    time.sleep(5) # Tunggu selama 5 detik sebelum menghentikan loop1
    loop1.stop() # Hentikan loop1 dari thread utama
    print("Loop 1 dihentikan.")

# Buat thread untuk menjalankan loop1
loop1_thread = threading.Thread(target=loop1)
loop1_thread.start()

# Jalankan loop2 dari thread utama
loop2()