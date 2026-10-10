class NEOAI:
    def __init__(self, nama, umur, tinggibadan):
        self.nama = nama
        self.umur = umur
        self.tinggibadan = tinggibadan
    def __str__(self):
        return f"Saham mayoritas NEO AI dipegang oleh {self.nama} dan beliau berumur {self.umur} tahun dan beliau memiliki tinggi badan {self.tinggibadan}"
    
    def __eq__(self, other):
        return self.umur == other.umur or self.nama == other.nama or self.tinggibadan == other.tinggibadan
    
    def __lt__(self, other):
        return self.umur < other.umur

    def __gt__(self, other):
        return self.umur > other.umur
    
    def __add__(self, other):
        return f"{self.tinggibadan + other.tinggibadan } kedua orang tersebut"
   
    def __contains__(self, keyword):
        return keyword in self.nama
     
    def __getitem__(self, key):
        if key == "nama":
            return self.nama
        elif key == "umur":
            return self.umur
        else:
            return f"the key is not found"
neo1 = NEOAI("Agastya", 18, 181)
neo2 = NEOAI("Sassy", 20, 169)
neo3 = NEOAI("Juun", 21, 173)

print(neo1 == neo2) # Output: False
print(neo2 < neo3)  # Output: True (Sekarang berjalan lancar!)
print(neo1>neo2) # output: False
print(neo1+neo2)
print("Agastya" in neo1)
print(neo2["nama"])
print(neo1["teddy"])