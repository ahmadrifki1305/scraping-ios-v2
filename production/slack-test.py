import datetime
import time
import os 

def coba1():
    

    waktu = "14:31:00"

    # Memisahkan waktu menjadi jam, menit, dan detik
    jam, menit, detik = waktu.split(":")
    jam = int(jam)
    menit = int(menit)
    detik = int(detik)
    # Membuat objek datetime dengan waktu yang telah dipisahkan
    waktu_objek = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, jam, menit, detik)
    
    # Membandingkan waktu dengan waktu saat ini
    if waktu_objek > datetime.datetime.now():
        print("Waktu", waktu, "belum tercapai")
    else:
        print("Waktu", waktu, "sudah tercapai atau sudah lewat")
        text = "t1"
        with open("output.txt", "w") as file:
            file.write(text)
    time.sleep(2)

def hapusfile():
    with open("output.txt", "r") as file:
        isi_file = file.read()
        print(isi_file)
        if isi_file == "t1" :
            namafile = "output.txt"
            os.remove(namafile)
            print("File", namafile, "telah dihapus.")

while True:
    coba1()
    hapusfile()
    continue


if __name__ == "__main__":
    # jalankan aplikasi utama
    print("Aplikasi dimulai")
    coba1()
  
   # print("Aplikasi selesai")