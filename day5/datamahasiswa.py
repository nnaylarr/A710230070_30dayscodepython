class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")

# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Nayla", "88856", "Informatika")
mahasiswa2 = Mahasiswa("Hurin", "99921", "Sistem Informasi")

# Menampilkan informasi mahasiswa
mahasiswa1.tampilkan_info()
print()
mahasiswa2.tampilkan_info()
