import time
print("=" * 50)
print("Selamat datang di neo ai".upper().center(50))
print("=" * 50)
time.sleep(3)
class NovaAI():
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.is_human = True
        self.akses_diterima = False
    def tampil_profil(self):
        print("\n---PROFIL PENGGUNA---")
        print(f"Nama    :{self.nama}") 
        print(f"Umur    :{self.umur} Tahun") 
        print("-" * 25)
    
    def cek_umur(self):
        print("\n[NEO AI] Memeriksa persyaratan umur.....")
        time.sleep(2)
        
        if self.umur < 18:
            print(f"[-]Maaf {self.nama}, Anda tidak diperbolehkan mengakses AI ini")
            print(f"Umur anda adalah {self.umur} Tahun")
            self.akses_diterima = False
        else:
            print(f"[+] Halo {self.nama}, Anda diperbolehkan mengakses AI ini")
            print(f"Umur anda adalah {self.umur} Tahun")
            self.akses_diterima = True
        
    def cek_akses(self):
        print("\n[NEO AI] telah memverivikasi data anda...")
        time.sleep(3)
        if self.is_human:
            print(
                f"[+] Identitas {self.nama} "
                "Berhasil diidentifikasi"
            )  
            print(
                f"[+] Status: Human"
            )
        else:
            print(
                f"[-] Akses denied untuk {self.nama}"
                "[-] Status: Bot"
            )
class pengguna():
    def __init__(self, gmail, password):
        self.gmail = gmail
        self.password = password
    def tampilkan(self):
        print("\n---INFORMASI PRIBADI GOOGLE---")
        print(f"Email   :{self.gmail}")
        print(f"Password    :{'*' * len(self.password)}")
    
    def verifikasi_password(self):
        print("\n NEO AI sedang memverikasi password anda....")
        time.sleep(3)
        
        panjang_password = len(self.password) >= 10
        
        any_number = any(
            karakter.isdigit()
            for karakter in self.password
        )
        any_letter_big = any(
            karakter.isupper()
            for karakter in self.password
        )
        if(
            panjang_password
            and any_number
            and any_letter_big
        ):
            print("[+] Password valid.")
            print("[+] Password memenuhi standar NEO AI")
            self.is_valid = True
            
        else:
            print("[-] Password tidak valid")
            time.sleep(0.5)
            print("[-] Password harus memiliki:")
            print("- Minimal 10 karakter")
            print("- Minimal 1 angka")
            print("- Minimal 1 huruf kapital")
            self.is_valid = False
            
gmail = input("Silahkan masukkan email anda: ")
password = input("Silahkan masukkan password anda: ")
akun = pengguna(gmail, password)
time.sleep(1)
akun.tampilkan()
akun.verifikasi_password()
user_nama = input("Silahkan masukkan nama anda: ")
user_umur = int(input("Silahkan masukkan umur anda: "))
neo = NovaAI(user_nama, user_umur)
neo.tampil_profil()
neo.cek_umur()
neo.cek_akses()



            