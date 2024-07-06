def main():
    # Harga tiket
    harga_vip = 150000
    harga_reguler = 75000
    
    print("Selamat datang di bioskop kami!")
    print("Pilih jenis tiket Anda:")
    print("1. VIP (Rp 150,000)")
    print("2. Reguler (Rp 75,000)")
    
    pilihan = int(input("Masukkan pilihan Anda (1 atau 2): "))
    
    if pilihan == 1:
        jenis_tiket = "VIP"
        harga = harga_vip
    elif pilihan == 2:
        jenis_tiket = "Reguler"
        harga = harga_reguler
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        return
    
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
    total_harga = jumlah_tiket * harga
    
    print(f"Anda telah memilih {jumlah_tiket} tiket {jenis_tiket}.")
    print(f"Total harga adalah: Rp {total_harga}")
    
    konfirmasi = input("Apakah Anda ingin melanjutkan pembelian? (ya/tidak): ")
    
    if konfirmasi.lower() == "ya":
        print("Pembelian berhasil! Terima kasih telah membeli tiket di bioskop kami.")
    else:
        print("Pembelian dibatalkan.")

if __name__ == "__main__":
    main()
