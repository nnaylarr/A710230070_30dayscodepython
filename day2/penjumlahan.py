def tambah(a, b):
    return a + b

def main():
    print("penjumlahan")

    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        hasil = tambah(num1, num2)
        print(f"Hasil: {num1} + {num2} = {hasil}")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

if __name__ == "__main__":
    main()
