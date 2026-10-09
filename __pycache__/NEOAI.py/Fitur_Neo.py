class NEOAI:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def __str__(self):
        return f"Saham mayoritas NEO AI dipegang oleh {self.nama} dan beliau berumur {self.umur} tahun"
    
    def __eq__(self, other):
        return self.umur == other.umur or self.nama == other.nama
    
    def __it__(self, other):
neo1 = NEOAI("Agastya", 18)
neo2 = NEOAI("Sassy", 20)
neo3 = NEOAI("Juun", 21)
print(neo1 == neo2)#perbandingan
