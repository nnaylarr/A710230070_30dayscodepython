def tambah_pengeluaran(pengeluaran, keterangan, jumlah):
    pengeluaran.append({'keterangan': keterangan, 'jumlah': jumlah})
    print(f"Pengeluaran '{keterangan}' sebesar {jumlah} berhasil ditambahkan.")

def tampilkan_pengeluaran(pengeluaran):
    if not pengeluaran:
        print("Tidak ada pengeluaran yang tercatat.")
        return
    print("\nDaftar Pengeluaran Harian:")
    total = 0
    for idx, item in enumerate(pengeluaran, start=1):
        print(f"{idx}. {item['keterangan']} - {item['jumlah']}")
        total += item['jumlah']
    print(f"Total Pengeluaran: {total}")

def main():
    pengeluaran = []
    
    while True:
        print("\nKalkulator Pengeluaran Harian")
        print("1. Tambah Pengeluaran")
        print("2. Tampilkan Pengeluaran")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            keterangan = input("Masukkan keterangan pengeluaran: ")
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            tambah_pengeluaran(pengeluaran, keterangan, jumlah)
        elif pilihan == '2':
            tampilkan_pengeluaran(pengeluaran)
        elif pilihan == '3':
            print("Terima kasih telah menggunakan kalkulator pengeluaran harian.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
