class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis

class Kucing(Hewan):
    def __init__(self, jenis, warna):
        super().__init__(jenis)
        self.warna = warna

class Anjing(Hewan):
    def __init__(self, jenis, ras):
        super().__init__(jenis)
        self.ras = ras

class Singa(Hewan):
    def __init__(self, jenis, habitat):
        super().__init__(jenis)
        self.habitat = habitat

kucing = Kucing("Kucing", "Putih")
anjing = Anjing("Anjing", "Bulldog")
singa = Singa("Singa", "Savannah")

print(f"{kucing.jenis}, Warna: {kucing.warna}")
print(f"{anjing.jenis}, Ras: {anjing.ras}")
print(f"{singa.jenis}, Habitat: {singa.habitat}")
