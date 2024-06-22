tasks = []

def show_tasks():
    print("Daftar Tugas Harian:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print(f"Tugas '{task}' telah ditambahkan!")

def delete_task():
    show_tasks()
    task_number = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
    if task_number < len(tasks):
        del tasks[task_number]
        print("Tugas telah dihapus!")
    else:
        print("Nomor tugas tidak valid!")

while True:
    print("\nMenu:")
    print("1. Tampilkan Daftar Tugas")
    print("2. Tambah Tugas Baru")
    print("3. Hapus Tugas")
    print("4. Keluar")
    choice = input("Pilih menu: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Menu tidak valid!")