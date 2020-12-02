"""
Program menghitung luas segitiga
Luas = Alas * tinggi /2
"""
print('Menghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2

print(f"segitiga dengan alas {alas} dan tinggi {tinggi} mempunyai luas {luas_segitiga}")

print('\nMenghitung luas segitiga 2 dengan copy paste')
alas = 10
tinggi = 3
luas_segitiga = alas * tinggi / 2

print(f"segitiga dengan alas {alas} dan tinggi {tinggi} mempunyai luas {luas_segitiga}")

print('\nMembuat fungsi menghitung luas segitiga')
def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 0
tinggi = 0
lanjut = "y"


while lanjut == "y":
    a = input('Masukan alas: ')
    t = input('Masukan tinggi: ')

    alas = float(a)
    tinggi = float(t)

    print(f"segitiga dengan alas {alas} dan tinggi {tinggi} mempunyai luas {hitung_luas_segitiga(alas, tinggi)}")
    print(f'Menghtung luas segitiga dengan fungsi, hasilnya {hitung_luas_segitiga(12, 12)}')
    lanjut = input('Menghtung luas segitiga lagi [y/t] : ')

print('\nTerimakasih sudah mencoba')

