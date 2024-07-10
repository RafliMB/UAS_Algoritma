class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def set_nama(self, nama_baru):
        self.nama = nama_baru

    def set_warna(self, warna_baru):
        self.warna = warna_baru

    def set_rasa(self, rasa_baru):
        self.rasa = rasa_baru
        
    def info(self):

class Mangga(Buah):
    def __init__(self, vitamin):
        Buah.__init__(self, nama, warna, rasa)
        self.vitamin = vitamin

    def set_vitamin(self, vitamin_baru):
        self.vitamin = vitamin_baru

    def info(self):
        return f'vitamin'