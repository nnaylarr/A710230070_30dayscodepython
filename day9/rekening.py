class RekeningBank:
    def __init__(self, nama_pemilik, saldo):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo

    def deposit(self, jumlah):
        self.saldo += jumlah
        print(f"Rp{jumlah} telah didepositkan. Saldo baru: Rp{self.saldo}")

    def penarikan(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        else:
            self.saldo -= jumlah
            print(f"Rp{jumlah} telah ditarik. Saldo baru: Rp{self.saldo}")

    def tampilkan_saldo(self):
        print(f"Saldo pemilik {self.nama_pemilik}: Rp{self.saldo}")

rekening1 = RekeningBank("Nayla", 1000000)


rekening1.tampilkan_saldo()

rekening1.deposit(230000)
rekening1.penarikan(730000)
rekening1.penarikan(4000000)
