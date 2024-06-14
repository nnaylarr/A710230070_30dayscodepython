def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Meminta input dari pengguna
batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

# Menampilkan bilangan prima dalam rentang
print(f"Bilangan prima antara {batas_bawah} dan {batas_atas} adalah:")
for num in range(batas_bawah, batas_atas + 1):
    if cek_prima(num):
        print(num)
