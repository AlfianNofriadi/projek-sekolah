class elektronik:
    def __init__(self, merk, harga, ram):
        self.merk = merk
        self.harga = harga
        self.ram = ram

    def info(self):
        return f"Merk: {self.merk}, Harga: {self.harga}, RAM: {self.ram} GB"

class laptop (elektronik):
    def __init__(self, merk, harga, ram, vga):
        super().__init__(merk, harga, ram)
        self.vga = vga

    def info(self):
        item_info = super().info()
        return f"{item_info}, VGA: {self.vga}"

print("")
print("Info Elektronik (Laptop):")
merk = input("Merk Laptop: ")
harga = int(input("Harga: "))
ram = int(input("RAM (GB): "))
vga = input("VGA: ")
lp = laptop(merk, harga, ram, vga)
print("")
print("------------------------------Hasil------------------------------")
print(lp.info())