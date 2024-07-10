data_mahasiswa = []

while True:
    nim = int(input("Masukkan NIM : "))
    nama = str(input("Masukkan nama : "))
    mahasiswa = {"nama" : nama, "nim" : nim}
    data_mahasiswa.append(mahasiswa)
    ulang = str(input("Ingin tambah lagi? (Ya/Tidak): ")).lower
    if ulang == "tidak":
        break

nomor = 1
for i in data_mahasiswa:
    print(f"{nomor}. Nama : {i['nama']}, NIM : {i['nim']}")
    nomor += 1