class Laptop:
    def __init__(self, merk, kualitas):
        self.merk = merk
        self.kualitas = kualitas

    def info_laptop(self):
        raise NotImplementedError("Subclasses harus mengimplementasikan metode ini")


class Dell(Laptop):
    def info_laptop(self):
        return f"Laptop merk {self.merk} dengan kualitas {self.kualitas}"


class HP(Laptop):
    def info_laptop(self):
        return f"Laptop merk {self.merk} dengan kualitas {self.kualitas}"


class Asus(Laptop):
    def info_laptop(self):
        return f"Laptop merk {self.merk} dengan kualitas {self.kualitas}"


# Fungsi yang menggunakan polymorphism
def tampilkan_info_laptop(laptop):
    print(laptop.info_laptop())


# Contoh penggunaan
laptop_dell = Dell("Dell", "Premium")
laptop_hp = HP("HP", "Menengah")
laptop_asus = Asus("Asus", "Ekonomis")

tampilkan_info_laptop(laptop_dell) 
tampilkan_info_laptop(laptop_hp)   
tampilkan_info_laptop(laptop_asus) 
