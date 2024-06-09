def main():
    print("Program Kalkulator Sederhana")
    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        
        print(f"Hasil penjumlahan: {num1 + num2}")
        print(f"Hasil pengurangan: {num1 - num2}")
        print(f"Hasil perkalian: {num1 * num2}")
        print(f"Hasil pembagian: {num1 / num2}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan.")
    
if __name__ == "__main__":
    main()
