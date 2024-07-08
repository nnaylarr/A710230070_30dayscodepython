mahasiswa = {
    "nama": "Andi",
    "umur": 25,
    "jurusan": "Informatika"
}

print("Nama:", mahasiswa["nama"])

mahasiswa["IPK"] = 3.75
print("Dictionary setelah penambahan:", mahasiswa)

del mahasiswa["umur"]
print("Dictionary setelah penghapusan:", mahasiswa)
