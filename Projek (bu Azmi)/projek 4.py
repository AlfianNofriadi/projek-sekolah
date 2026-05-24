class  SuzukiErtiga2018:
    def __init__(self, merk, mesin, warna, tahun):
        self.merk = merk
        self.mesin = mesin
        self.warna = warna
        self.tahun = tahun
    
    def info(self):
        print("Merk",self.merk,"dengan mesin", self.mesin,"dan berwarna", self.warna,"serta keluaran tahun", self.tahun)

mobil1 = SuzukiErtiga2018("Suzuki Ertiga,", " 1.5L K15B,", " Hitam,", 2018)
mobil1.info()


class SuzukiErtiga2023(SuzukiErtiga2018):
    pass

mobil2 = SuzukiErtiga2023("Suzuki Ertiga,", " 1.5L K15B Smart Hybrid,", " Putih,", 2023)
mobil2.info()