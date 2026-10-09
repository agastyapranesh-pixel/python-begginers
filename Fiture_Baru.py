import time

class Asset:
    def __init__(self, nama_asset, jumlah, harga_beli, harga_sekarang):
        self.nama_asset = nama_asset
        self.jumlah = jumlah
        self.harga_beli = harga_beli
        self.harga_sekarang = harga_sekarang

    def modal(self):
        return self.jumlah * self.harga_beli

    def nilaisekarang(self):
        return self.jumlah * self.harga_sekarang

    def Profit_Loss(self):
        return self.nilaisekarang() - self.modal()

    def breakEven(self):
        if self.Profit_Loss() > 0:
            return "PROFIT"
        elif self.Profit_Loss() < 0:
            return "LOSS"
        else:
            return "BREAK EVEN"

    def Return(self):
        if self.modal() == 0:
            return 0.0
        return (self.Profit_Loss() / self.modal()) * 100


class FiturTambahan:
    def jalankan(self):
        time.sleep(1)
        print("=" * 50)
        print("PROFIT / LOSS CALCULATOR".center(50))
        print("=" * 50)

        nama_asset = input("Silahkan masukkan tipe asset anda: ")
        jumlah = int(input("Silahkan masukkan jumlah asset yang anda investasikan: "))
        harga_beli = float(input("Silahkan input harga beli asset anda: "))
        harga_sekarang = float(input("Silahkan input harga sekarang asset anda: "))

        asset = Asset(nama_asset, jumlah, harga_beli, harga_sekarang)

        modal = asset.modal()
        nilai_sekarang = asset.nilaisekarang()
        profit_loss = asset.Profit_Loss()
        status = asset.breakEven()
        return_percentage = asset.Return()

        print("\n" + "=" * 50)
        print("DATA ASSET".center(50))
        print("=" * 50)

        print(f"Asset          : {asset.nama_asset}")
        print(f"Jumlah         : {asset.jumlah}")
        print(f"Harga Beli     : Rp{asset.harga_beli:,.2f}")
        print(f"Harga Sekarang : Rp{asset.harga_sekarang:,.2f}")

        print("-" * 50)
        print(f"Modal          : Rp{modal:,.2f}")
        print(f"Nilai Sekarang : Rp{nilai_sekarang:,.2f}")
        print(f"Profit/Loss    : Rp{profit_loss:,.2f} ({status})")
        print(f"Return (%)     : {return_percentage:,.2f}%")
        print("=" * 50)
        
        time.sleep(1.5)
        print("=" * 50)
        print("WISHLIST NOVA AI".center(50))
        print("=" * 50)
        
        print("=" * 50)
        print("MODUL KONVERSI MATA UANG KRIPTO".center(50))
        print("=" * 50)
        time.sleep(2)
        
print("=" * 50)
print("Konversi Mata Uang".center(50).upper())
print("=" * 50)
time.sleep(3)
class Konversi:
    def __init__(self):
        # Dictionary penyimpan harga koin dalam USD
        self.harga_koin = {
            "BTC": 60000,
            "ETH": 3000,
            "SOL": 140,
            "BNB": 500
        }
        # Nilai tukar (Kurs)
        self.kurs_idr = 15500  
        
    def hitung_konversi(self, koin, jumlah, pilihan_mata_uang):
        # Mengubah input koin dan mata uang menjadi huruf besar semua agar cocok (misal: btc -> BTC)
        koin = koin.upper()
        pilihan_mata_uang = pilihan_mata_uang.upper()
        
        if koin not in self.harga_koin:
            return "[-] Koin tidak ditemukan di database NOVA AI!"
            
        total_usd = jumlah * self.harga_koin[koin]
        
        if pilihan_mata_uang == "IDR":
            total_idr = total_usd * self.kurs_idr
            return f"[+] Hasil: {jumlah} {koin} = Rp{total_idr:,.2f}"
            
        elif pilihan_mata_uang == "USD":
            return f"[+] Hasil: {jumlah} {koin} = ${total_usd:,.2f}"
            
        else:
            return "[-] Mata uang tidak dikenali! Pilih IDR atau USD."
time.sleep(3)
print("=" * 50)
print("Program Selesai".upper().center(50))
print("=" * 50)