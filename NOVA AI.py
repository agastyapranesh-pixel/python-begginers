import time
import random
import Fiture_Baru

# ==================================================
#                  NOVA AI
# ==================================================


print("=" * 55)
print("                 SELAMAT DATANG")
print("                   NOVA AI")
print("=" * 55)
print()


# ==================================================
#                  CLASS NOVA AI
# ==================================================

class NovaAI:

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.is_human = True
        self.akses_diterima = False
        
    
    def perkenalkan(self):
        print("\n--- PROFIL PENGGUNA ---")
        print(f"Nama       : {self.nama}")
        print(f"Umur       : {self.umur} Tahun")
        print("-" * 25)

    def cek_umur(self):

        print("\n[NOVA AI] Memeriksa persyaratan umur...")
        time.sleep(1)

        if self.umur < 18:

            print(
                f"[-] Maaf, {self.nama}."
                f" Umur kamu {self.umur} tahun."
            )

            print(
                "[-] Kamu belum memenuhi"
                " persyaratan akses NOVA AI."
            )

            self.akses_diterima = False

        else:

            print(
                f"[+] Umur {self.umur} tahun"
                " memenuhi persyaratan."
            )

            self.akses_diterima = True

    def cek_akses(self):

        print("\n[NOVA AI] Memverifikasi identitas...")
        time.sleep(3)

        if self.is_human:

            print(
                f"[+] Identitas {self.nama}"
                " berhasil diverifikasi."
            )

            print("[+] Status: HUMAN")

        else:

            print(
                f"[-] Akses ditolak untuk {self.nama}."
            )

            print("[!] Status: BOT")


# ==================================================
#                  CLASS AKUN
# ==================================================

class AkunPengguna:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def tampilkan(self):

        print("\n--- INFORMASI AKUN ---")
        print(f"Email    : {self.email}")
        print(
            f"Password : {'*' * len(self.password)}"
        )


class AkunNOVAAI(AkunPengguna):

    def __init__(self, email, password, nama_akun):

        super().__init__(email, password)

        self.nama_akun = nama_akun
        self.is_valid = False

    def validasi_password(self):

        print("\n[NOVA AI] MEMVALIDASI PASSWORD...")
        time.sleep(3)

        panjang_password = len(self.password) >= 10

        ada_angka = any(
            karakter.isdigit()
            for karakter in self.password
        )

        ada_huruf_besar = any(
            karakter.isupper()
            for karakter in self.password
        )

        if (
            panjang_password
            and ada_angka
            and ada_huruf_besar
        ):

            print("[+] Password valid.")
            print("[+] Password memenuhi semua syarat.")

            self.is_valid = True

        else:

            print("[-] Password tidak valid.")
            print()
            print("Password harus memiliki:")
            print("- Minimal 10 karakter")
            print("- Minimal 1 angka")
            print("- Minimal 1 huruf kapital")

            self.is_valid = False


# ==================================================
#                  CLASS CRYPTO
# ==================================================

class Altcoin:

    def __init__(self):

        self.daftar_altcoin = [
            "Ethereum (ETH)",
            "Solana (SOL)",
            "Binance Coin (BNB)",
            "Cardano (ADA)",
            "Avalanche (AVAX)"
        ]

    def analisis(self, pertanyaan):

        print(
            "\n[NOVA AI] Menganalisis pertanyaan"
            " seputar cryptocurrency..."
        )

        time.sleep(1.5)

        pertanyaan = pertanyaan.lower()

        # ------------------------------------------
        # Rule sederhana
        # ------------------------------------------

        if "ethereum" in pertanyaan or "eth" in pertanyaan:

            rekomendasi = "Ethereum (ETH)"

        elif "solana" in pertanyaan or "sol" in pertanyaan:

            rekomendasi = "Solana (SOL)"

        elif "bnb" in pertanyaan:

            rekomendasi = "Binance Coin (BNB)"

        elif "cardano" in pertanyaan or "ada" in pertanyaan:

            rekomendasi = "Cardano (ADA)"

        elif "avalanche" in pertanyaan or "avax" in pertanyaan:

            rekomendasi = "Avalanche (AVAX)"

        else:

            rekomendasi = random.choice(
                self.daftar_altcoin
            )

        print()
        print("[NOVA AI] Hasil simulasi:")
        print(f"Asset yang terdeteksi : {rekomendasi}")

        print(
            "\n[!] Catatan:"
            " hasil ini hanya simulasi"
            " dan bukan nasihat investasi."
        )

        return rekomendasi


# ==================================================
#                  CLASS PORTFOLIO
# ==================================================

class Portfolio:

    def __init__(self):

        self.assets = []

    def tambah_asset(self):

        print("\n" + "=" * 40)
        print("             TAMBAH ASSET")
        print("=" * 40)

        nama_asset = input(
            "Nama asset: "
        ).upper()

        while True:

            try:

                jumlah = float(
                    input("Jumlah asset: ")
                )

                if jumlah > 0:
                    break

                print(
                    "Jumlah harus lebih dari 0."
                )

            except ValueError:

                print(
                    "Masukkan angka yang valid."
                )

        while True:

            try:

                harga = float(
                    input("Harga per asset: Rp")
                )

                if harga > 0:
                    break

                print(
                    "Harga harus lebih dari 0."
                )

            except ValueError:

                print(
                    "Masukkan angka yang valid."
                )

        asset = {
            "nama": nama_asset,
            "jumlah": jumlah,
            "harga": harga
        }

        self.assets.append(asset)

        print(
            f"\n[+] {nama_asset}"
            " berhasil ditambahkan."
        )

    def tampilkan_portfolio(self):

        print("\n" + "=" * 50)
        print("              PORTFOLIO")
        print("=" * 50)

        if not self.assets:

            print(
                "\nPortfolio masih kosong."
            )

            return

        total = 0

        for nomor, asset in enumerate(
            self.assets,
            start=1
        ):

            nilai = (
                asset["jumlah"]
                * asset["harga"]
            )

            total += nilai

            print(
                f"\n{nomor}. {asset['nama']}"
            )

            print(
                f"   Jumlah : {asset['jumlah']}"
            )

            print(
                f"   Harga  : Rp{asset['harga']:,.2f}"
            )

            print(
                f"   Nilai  : Rp{nilai:,.2f}"
            )

        print("\n" + "-" * 50)

        print(
            f"Total Portfolio : Rp{total:,.2f}"
        )

    def menu_portfolio(self):

        while True:

            print("\n" + "=" * 50)
            print("             NOVA PORTFOLIO")
            print("=" * 50)

            print("[1] Tambah Asset")
            print("[2] Lihat Portfolio")
            print("[3] Kembali")

            pilihan = input(
                "\nPilih menu: "
            )

            if pilihan == "1":

                self.tambah_asset()

            elif pilihan == "2":

                self.tampilkan_portfolio()

            elif pilihan == "3":

                break

            else:

                print(
                    "\n[-] Pilihan tidak tersedia."
                )


# ==================================================
#                  CLASS HISTORY
# ==================================================

class History:

    def __init__(self):

        self.data = []

    def tambah_history(self, aktivitas):

        self.data.append(aktivitas)

    def tampilkan_history(self):

        print("\n" + "=" * 50)
        print("               HISTORY")
        print("=" * 50)

        if not self.data:

            print(
                "\nBelum ada aktivitas."
            )

            return

        for nomor, aktivitas in enumerate(
            self.data,
            start=1
        ):

            print(
                f"{nomor}. {aktivitas}"
            )


# ==================================================
#                  CLASS SETTINGS
# ==================================================

class Settings:

    def __init__(self):

        self.mode = "Default"

    def menu_settings(self):

        while True:

            print("\n" + "=" * 50)
            print("               SETTINGS".center())
            print("=" * 50)

            print(
                f"Current Mode : {self.mode}"
            )

            print()
            print("[1] Default Mode")
            print("[2] Developer Mode")
            print("[3] Kembali")

            pilihan = input(
                "\nPilih menu: "
            )

            if pilihan == "1":

                self.mode = "Default"

                print(
                    "[+] Default Mode aktif."
                )

            elif pilihan == "2":

                self.mode = "Developer"

                print(
                    "[+] Developer Mode aktif."
                )

            elif pilihan == "3":

                break

            else:

                print(
                    "[-] Pilihan tidak tersedia."
                )


# ==================================================
#                  MAIN MENU
# ==================================================

class MenuNovaAI:

    def __init__(
        self,
        pengguna,
        akun,
        crypto,
        portfolio,
        history,
        settings
    ):

        self.pengguna = pengguna
        self.akun = akun
        self.crypto = crypto
        self.portfolio_data = portfolio
        self.history_data = history
        self.settings_data = settings

    def tampilkan_menu(self):

        while True:

            print("\n" + "=" * 55)
            print("                    NOVA AI")
            print("=" * 55)

            print(
                f"\nHalo, {self.pengguna.nama}!"
            )

            print("\n[1] 👤 Profile")
            print("[2] 🤖 AI Assistant")
            print("[3] ₿  Crypto Analysis")
            print("[4] 📊 Portfolio")
            print("[5] 📜 History")
            print("[6] ⚙️  Settings")
            print("[7] 🧮 Profit/Loss Calculator")
            print("[8] 🚪 Logout")

            print("=" * 55)

            pilihan = input(
                "Pilih menu: "
            )

            if pilihan == "1":

                self.profil()

            elif pilihan == "2":

                self.ai_assistant()

            elif pilihan == "3":

                self.crypto_analysis()

            elif pilihan == "4":

                self.portfolio()

            elif pilihan == "5":

                self.history()

            elif pilihan == "6":

                self.settings()

            elif pilihan == "7":
                
                self.history_data.tambah_history("Profit/Loss Calculator dibuka")
                objek_fitur = Fiture_Baru.FiturTambahan()
                objek_fitur.jalankan()

            elif pilihan == "8":

                print(
                    "\n[NOVA AI] Logging out..."
                )

                time.sleep(1)

                print(
                    "[+] Logout berhasil."
                )

                break

            else:

                print(
                    "\n[-] Pilihan tidak tersedia."
                )

    # ------------------------------------------------
    # PROFILE
    # ------------------------------------------------

    def profil(self):

        print("\n" + "=" * 45)
        print("                 PROFILE")
        print("=" * 45)

        print(
            f"Nama          : {self.pengguna.nama}"
        )

        print(
            f"Umur          : {self.pengguna.umur}"
        )

        print(
            f"Email         : {self.akun.email}"
        )

        print(
            f"Nama Akun     : {self.akun.nama_akun}"
        )

        print(
            f"Status Akses  : "
            f"{'Aktif' if self.pengguna.akses_diterima else 'Tidak Aktif'}"
        )

    # ------------------------------------------------
    # AI ASSISTANT
    # ------------------------------------------------

    def ai_assistant(self):

        print("\n" + "=" * 50)
        print("               NOVA AI ASSISTANT")
        print("=" * 50)

        print(
            "\n[NOVA AI] AI Assistant masih"
            " dalam tahap pengembangan."
        )

        print(
            "\nUntuk sementara kamu dapat"
            " menggunakan Crypto Analysis."
        )

        self.history_data.tambah_history(
            "AI Assistant dibuka"
        )

    # ------------------------------------------------
    # CRYPTO ANALYSIS
    # ------------------------------------------------

    def crypto_analysis(self):

        print("\n" + "=" * 50)
        print("             CRYPTO ANALYSIS")
        print("=" * 50)

        pertanyaan = input(
            "\nMasukkan pertanyaan crypto:\n> "
        )

        hasil = self.crypto.analisis(
            pertanyaan
        )

        self.history_data.tambah_history(
            f"Crypto Analysis digunakan: {hasil}"
        )

    # ------------------------------------------------
    # PORTFOLIO
    # ------------------------------------------------

    def portfolio(self):

        self.history_data.tambah_history(
            "Portfolio dibuka"
        )

        self.portfolio_data.menu_portfolio()

    # ------------------------------------------------
    # HISTORY
    # ------------------------------------------------

    def history(self):

        self.history_data.tampilkan_history()

    # ------------------------------------------------
    # SETTINGS
    # ------------------------------------------------

    def settings(self):

        self.settings_data.menu_settings()

        self.history_data.tambah_history(
            "Settings dibuka"
        )


# ==================================================
#                  PROGRAM UTAMA
# ==================================================

nama_input = input(
    "Silahkan input nama Anda : "
)


# ==================================================
#                  VALIDASI UMUR
# ==================================================

while True:

    try:

        umur_input = int(
            input(
                "Silahkan input umur Anda : "
            )
        )

        if umur_input > 0:

            break

        print(
            "[-] Umur harus lebih dari 0."
        )

    except ValueError:

        print(
            "[-] Masukkan umur dalam bentuk angka."
        )


# ==================================================
#                  USER OBJECT
# ==================================================

pengguna = NovaAI(
    nama_input,
    umur_input
)

pengguna.cek_umur()


# ==================================================
#                  CEK AKSES
# ==================================================

if pengguna.akses_diterima:

    pengguna.cek_akses()
    pengguna.perkenalkan()

else:

    print(
        "\n[NOVA AI] Program dihentikan."
    )

    exit()


# ==================================================
#                  REGISTRASI AKUN
# ==================================================

print("\n" + "=" * 55)
print("             REGISTRASI AKUN NOVA AI")
print("=" * 55)

DataEmail = input(
    "\nSilahkan input email Anda: "
)

DataPassword = input(
    "Silahkan input password Anda: "
)


Data = AkunNOVAAI(
    DataEmail,
    DataPassword,
    "NovaAI"
)


Data.validasi_password()


if not Data.is_valid:

    print(
        "\n[NOVA AI] Registrasi gagal."
    )

    print(
        "[NOVA AI] Program dihentikan."
    )

    exit()


Data.tampilkan()


# ==================================================
#                  MEMBUAT MODULE
# ==================================================

crypto = Altcoin()

portfolio = Portfolio()

history = History()

settings = Settings()


# ==================================================
#                  HISTORY AWAL
# ==================================================

history.tambah_history(
    "User berhasil login ke NOVA AI"
)

history.tambah_history(
    "Password berhasil divalidasi"
)


# ==================================================
#                  MAIN MENU
# ==================================================

menu = MenuNovaAI(
    pengguna,
    Data,
    crypto,
    portfolio,
    history,
    settings
)

menu.tampilkan_menu()


# ==================================================
#                  PROGRAM SELESAI
# ==================================================

print("\n" + "=" * 55)
print("              NOVA AI SELESAI")
print("=" * 55)

print(
    f"Terima kasih telah menggunakan NOVA AI,"
    f" {pengguna.nama}."
)

print("=" * 55)