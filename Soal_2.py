import pandas as pd

nilai_mahasiswa = {
    'mahasiswa 1' : [90, 80],
    'mahasiswa 2' : [50, 60],
    'mahasiswa 3' : [65, 70]
}

df = pd.DataFrame(nilai_mahasiswa)
print(df)