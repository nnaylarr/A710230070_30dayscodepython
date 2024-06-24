class RekeningBank:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.__saldo = saldo  

    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            return True
        return False

    def tarik_tunai(self, jumlah):
        if 0 < jumlah <= self.__saldo: 
            self.__saldo -= jumlah
            return True
        return False

    def get_saldo(self):
        return self.__saldo

rekening = RekeningBank("Nayla", 4000)
rekening.deposit(500)
print(rekening.get_saldo()) 
print(rekening.tarik_tunai(2000)) 
print(rekening.get_saldo())  
