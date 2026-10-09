import time
class Karyawan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    @classmethod
    def dari_tahun_lahir(cls, nama, tahun_lahir_karyawan):
        # Menggunakan tahun saat ini (2026) untuk menghitung umur
        tahun_sekarang = 2026 
        umur = tahun_sekarang - tahun_lahir_karyawan
        
        # Mengembalikan instance/objek baru dari class ini
        return cls(nama, umur)

# Cara penggunaan:
karyawan1 = Karyawan.dari_tahun_lahir("Agastya", 2008)

print(karyawan1.nama)  
print(karyawan1.umur)  
time.sleep(1.5)

class pemesanan:
    def __init__(self, Nama_kopi, Harga_Rupiah):
        self.Nama_kopi = Nama_kopi
        self.Harga_Rupiah = Harga_Rupiah
        
    @classmethod
    def gelas (cls, Nama_kopi, Ukuran_Gelas):
        if Ukuran_Gelas == "Small":
            Harga_Rupiah = 15000
        elif Ukuran_Gelas == "Medium":
            Harga_Rupiah = 20000
        elif Ukuran_Gelas == "Large":
            Harga_Rupiah = 25000
        else:
            Harga_Rupiah = 0
        return cls (Nama_kopi, Ukuran_Gelas)
Kopi_user = input("Masukkan nama kopi pilihan anda: ")
Ukuran_user = input("Masukkan Ukuran kopi pilihan anda (Small/Medium?Large): ")
customer1 = pemesanan.gelas(Kopi_user, Ukuran_user)
time.sleep(1.5)
print(f"Menu kopi anda: {customer1.Nama_kopi}")
print(f"Ukuran gelas anda: Rp {customer1.Harga_Rupiah}")
