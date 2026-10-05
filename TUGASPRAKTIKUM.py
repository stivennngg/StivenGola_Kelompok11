print("=" * 50)
print("Kelompok 11 Shift 2")
print("Raditya Bisma Wirayudha NIM : 21120126120010")
print("Yemima Regatha Hutapea NIM : 2112016120017")
print("Vabyano Novariyanto NIM : 21120126120025")
print("Stiven Gola NIM : 21120126140180")
print("=" * 50)

def pilih_menu() -> str:
    print("\n===== ANTREAN SERVIS ELEKTRONIK KELOMPOK 11 =====")
    print("1. Daftarkan servis")
    print("2. Lihat daftar servis")
    print("3. Mulai antrean berikutnya")
    print("4. Selesaikan servis")
    print("5. Cari data servis")
    print("6. Keluar")
    return input("Pilih menu (1-6): ").strip()

def cari_servis(daftar: list, nomor: str) -> int:
    nomor = nomor.strip().upper()

    for i in range(len(daftar)):
        if daftar[i]["nomor"] == nomor:
            return i

    return -1

class AntreanServis:
    def __init__(self) -> None:
        self.daftar = []
        self.nomor_berikutnya = 1

    def tambah_servis(self, nama: str, perangkat: str, keluhan: str) -> None:
        if nama == "" or perangkat == "" or keluhan == "":
            print("Pendaftaran gagal: semua data wajib diisi.")
        else:
            nomor = "A" + str(self.nomor_berikutnya).zfill(3)

            data = {
                "nomor": nomor,
                "nama": nama,
                "perangkat": perangkat,
                "keluhan": keluhan,
                "status": "Menunggu"
            }

            self.daftar.append(data)
            self.nomor_berikutnya += 1

            print(f"Servis berhasil didaftarkan. Nomor: {nomor}")

    def tampilkan_daftar(self) -> None:
        if len(self.daftar) == 0:
            print("Belum ada data servis.")
        else:
            print("\n===== DAFTAR SERVIS =====")

            for data in self.daftar:
                print(f"Nomor     : {data['nomor']}")
                print(f"Pelanggan : {data['nama']}")
                print(f"Perangkat : {data['perangkat']}")
                print(f"Keluhan   : {data['keluhan']}")
                print(f"Status    : {data['status']}")
                print("-" * 30)

    def mulai_servis(self) -> None:
        indeks = -1

        for i in range(len(self.daftar)):
            if self.daftar[i]["status"] == "Menunggu":
                indeks = i
                break

        if indeks == -1:
            print("Tidak ada servis yang menunggu.")
        else:
            self.daftar[indeks]["status"] = "Dikerjakan"
            nomor = self.daftar[indeks]["nomor"]

            print(f"Servis {nomor} mulai dikerjakan.")

    def selesaikan_servis(self, nomor: str) -> None:
        indeks = cari_servis(self.daftar, nomor)

        if indeks == -1:
            print("Nomor servis tidak ditemukan.")

        elif self.daftar[indeks]["status"] != "Dikerjakan":
            print("Hanya servis berstatus Dikerjakan yang bisa diselesaikan.")

        else:
            self.daftar[indeks]["status"] = "Selesai"
            nomor = self.daftar[indeks]["nomor"]

            print(f"Servis {nomor} sudah selesai.")

sistem = AntreanServis()

while True:
    pilihan = pilih_menu()

    if pilihan == "1":
        nama = input("Nama pelanggan : ").strip()
        perangkat = input("Jenis perangkat: ").strip()
        keluhan = input("Keluhan        : ").strip()

        sistem.tambah_servis(nama, perangkat, keluhan)

    elif pilihan == "2":
        sistem.tampilkan_daftar()

    elif pilihan == "3":
        sistem.mulai_servis()

    elif pilihan == "4":
        nomor = input("Nomor servis yang selesai: ")
        sistem.selesaikan_servis(nomor)

    elif pilihan == "5":
        nomor = input("Nomor servis yang dicari: ")
        indeks = cari_servis(sistem.daftar, nomor)

        if indeks == -1:
            print("Nomor servis tidak ditemukan.")
        else:
            data = sistem.daftar[indeks]

            print(f"Nomor     : {data['nomor']}")
            print(f"Pelanggan : {data['nama']}")
            print(f"Perangkat : {data['perangkat']}")
            print(f"Keluhan   : {data['keluhan']}")
            print(f"Status    : {data['status']}")

    elif pilihan == "6":
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak valid. Masukkan angka 1 sampai 6.")