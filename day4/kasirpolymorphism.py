class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def hitung_total(self, jumlah):
        return self.harga * jumlah

class BarangElektronik(Barang):
    def __init__(self, nama, harga, garansi):
        super().__init__(nama, harga)
        self.garansi = garansi

    def hitung_total(self, jumlah):
        total = super().hitung_total(jumlah)
        # Tambahkan pajak elektronik 10%
        total += total * 0.10
        return total

class BarangMakanan(Barang):
    def __init__(self, nama, harga, tanggal_kadaluarsa):
        super().__init__(nama, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def hitung_total(self, jumlah):
        total = super().hitung_total(jumlah)
        # Tambahkan pajak makanan 5%
        total += total * 0.05
        return total

def tampilkan_total_penjualan(barang, jumlah):
    total = barang.hitung_total(jumlah)
    print(f"Total harga untuk {jumlah} {barang.nama} adalah: Rp{total:.2f}")

elektronik = BarangElektronik("Laptop", 10000000, "2 Tahun")
makanan = BarangMakanan("Roti", 20000, "2024-12-31")

tampilkan_total_penjualan(elektronik, 2)
tampilkan_total_penjualan(makanan, 5)

