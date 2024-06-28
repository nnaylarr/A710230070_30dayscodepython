import time
from datetime import datetime, timedelta

def pengingat_minum_air():
    jam_mulai = 9 
    jam_kerja = 7 
    interval = 1 

    sekarang = datetime.now()
    waktu_mulai = sekarang.replace(hour=jam_mulai, minute=0, second=0, microsecond=0)
    waktu_selesai = waktu_mulai + timedelta(hours=jam_kerja)

    if sekarang > waktu_selesai:
        print("Jam kerja sudah selesai untuk hari ini.")
        return

    print("Program pengingat minum air dimulai...")
    waktu_berikutnya = waktu_mulai

    while waktu_berikutnya <= waktu_selesai:
        waktu_sekarang = datetime.now()
        if waktu_sekarang >= waktu_berikutnya:
            print(f"Pengingat: Saatnya minum air! ({waktu_sekarang.strftime('%H:%M:%S')})")
            waktu_berikutnya += timedelta(hours=interval)
        time.sleep(60)  

    print("Jam kerja telah selesai. Program pengingat minum air berhenti.")

pengingat_minum_air()
